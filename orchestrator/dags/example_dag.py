from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def example_task():
    print("This is an example DAG task.")


with DAG(
    dag_id="example_dag",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:
    t1 = PythonOperator(task_id="print_hello", python_callable=example_task)
