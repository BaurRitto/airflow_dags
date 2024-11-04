
'''
Runs call procedure from snowflake
'''

from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.utils.dates import days_ago
from datetime import timedelta


default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    'snowflake_copy_python_procedure_dag',
    default_args=default_args,
    description='DAG to call Python Snowflake procedure for data loading',
    schedule_interval='@daily',  # Adjust as needed
    catchup=False,
) as dag:

    # Call the stored procedure in Snowflake
    call_python_procedure = SnowflakeOperator(
        task_id='call_snowflake_python_procedure',
        snowflake_conn_id='snowflake_con',  # Connection ID defined in Airflow
        sql="SELECT 1;",
    )

    # Define the task
    call_python_procedure
