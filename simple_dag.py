"""
This is a simple DAG example for Apache Airflow.
"""

from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# Define a simple Python function
def print_message():
    """Prints a test message."""
    print("Hello, this is a test message from Airflow!")

# Define the DAG and its settings
with DAG(
    dag_id="simple_dag",
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    # Define the task
    hello_task = PythonOperator(
        task_id="hello_task",
        python_callable=print_message
    )
