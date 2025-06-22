import pandas as pd
from pyspark.sql import DataFrame
from pyspark.sql import functions as F

pd.set_option("display.max_columns", 500)


def assign_category_labels(
    df: DataFrame, category_column: str, categories: list
) -> DataFrame:
    """
    Assign integer labels to categorical values in the specified column.
    Null values are assigned -1, and unexpected categories will raise an error.

    Parameters:
    - df: The input Spark DataFrame.
    - category_column: The name of the categorical column in the DataFrame.
    - categories: A list of valid categories (must not be empty).

    Returns:
    - DataFrame with a new column 'category_index' containing the integer labels.
    """

    if not categories:
        raise ValueError(
            "Error: The list of categories is empty. Please define valid categories."
        )

    categories = [category.replace(",", "_COMMA_") for category in categories]

    categories_str = ",".join(categories)

    expr = f"""
        CASE 
            WHEN {category_column} IS NULL THEN -1 
            WHEN FIND_IN_SET(REPLACE({category_column}, ',', '_COMMA_'), '{categories_str}') > 0 
                THEN CAST(FIND_IN_SET(REPLACE({category_column}, ',', '_COMMA_'), '{categories_str}') - 1 AS INT)
            ELSE NULL -- No need for 'unexpected_category' here
        END AS category_index
    """

    df = df.withColumn(f"{category_column}_index", F.expr(expr))

    unexpected_category_found = (
        df.filter(F.col(f"{category_column}_index").isNull()).limit(1).count()
    )

    if unexpected_category_found > 0:
        raise ValueError("Error: There are unexpected categories in the data.")
    return df


# https://chatgpt.com/c/683a007a-47d0-8007-bd86-2df50a28de8a


def assign_grouped_category_labels(
    df: DataFrame, category_column: str, categories_mapping: dict
) -> DataFrame:
    """
    Assign integer labels to grouped categorical values based on a mapping.

    Parameters:
    - df: Input Spark DataFrame.
    - category_column: Name of the categorical column.
    - categories_mapping: Dict mapping new grouped category names to lists of raw category values.

    Returns:
    - DataFrame with new column: {category_column}_grouped_index
    """

    if not categories_mapping:
        raise ValueError(
            "Error: The category mapping is empty. Please provide valid mappings."
        )

    # Build reverse lookup: raw_category -> group_key
    reverse_map = {}
    for group, raw_list in categories_mapping.items():
        for raw in raw_list:
            raw_clean = raw.replace(",", "_COMMA_")
            if raw_clean in reverse_map:
                raise ValueError(f"Duplicate raw category '{raw}' in mapping.")
            reverse_map[raw_clean] = group

    # Replace commas in values and group keys
    group_keys = list(categories_mapping.keys())
    group_keys_cleaned = [k.replace(",", "_COMMA_") for k in group_keys]
    group_to_index = {k: i for i, k in enumerate(group_keys_cleaned)}

    # Build the CASE WHEN SQL expression
    case_expr = "CASE\n"
    case_expr += f"  WHEN {category_column} IS NULL THEN -1\n"

    for raw_value, group in reverse_map.items():
        index = group_to_index[group.replace(",", "_COMMA_")]
        case_expr += f"  WHEN REPLACE({category_column}, ',', '_COMMA_') = '{raw_value}' THEN {index}\n"

    case_expr += "  ELSE NULL\nEND"

    new_column = f"{category_column}_grouped_index"
    df = df.withColumn(new_column, F.expr(case_expr))

    # Check for unexpected categories
    if (
        df.filter(F.col(new_column).isNull() & F.col(category_column).isNotNull())
        .limit(1)
        .count()
        > 0
    ):
        raise ValueError(
            "Error: There are unexpected categories in the data not present in the mapping."
        )

    return df
