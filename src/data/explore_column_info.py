import pyspark
from pyspark.sql import functions as F
from pyspark.sql.functions import col, countDistinct, when


def get_column_summary(df: pyspark.sql.dataframe.DataFrame, column_name: str):
    # Get column data type
    dtype = str(df.schema[column_name].dataType)

    # Get count of distinct values in the column
    unique_values = df.select(countDistinct(col(column_name))).collect()[0][0]

    # Get count of null values in the column
    null_count = df.filter(col(column_name).isNull()).count()

    # Get total number of rows in the dataframe
    total_rows = df.count()

    # Calculate percentage of null values
    null_percentage = (null_count / total_rows) * 100

    top_5_values = (
        df.groupBy(column_name)
        .agg(F.count(column_name).alias("count"))
        .orderBy(F.col("count").desc())
        .limit(5)
    )

    min_value = df.select(F.min(column_name)).collect()[0][0]
    max_value = df.select(F.max(column_name)).collect()[0][0]

    # Print the column summary
    print(f"Summary for column: {column_name}")
    print("=" * 40)
    print(f"Data Type        : {dtype}")
    print(f"Unique Values    : {unique_values}")
    print(f"Null Count       : {null_count}")
    print(f"Total Rows       : {total_rows}")
    print(f"Null Percentage  : {null_percentage} %")
    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")
    print(
        f"Top 5 unique values : {[value[column_name] for value in top_5_values.collect()]}"
    )
    print("=" * 40)


def count_nulls(df):
    null_counts = (
        df.select(
            [sum(when(col(c).isNull(), 1).otherwise(0)).alias(c) for c in df.columns]
        )
        .collect()[0]
        .asDict()
    )

    print("Null values count per column:")
    for col_name, null_count in null_counts.items():
        print(f" - {col_name}: {null_count}")
