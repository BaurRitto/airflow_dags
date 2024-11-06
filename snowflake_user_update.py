
'''
Runs call procedure from snowflake
'''
from datetime import timedelta
from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.utils.dates import days_ago



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
    schedule_interval=None,  # Adjust as needed
    catchup=False,
) as dag:

    # Call the stored procedure in Snowflake
    call_python_procedure = SnowflakeOperator(
        task_id='call_snowflake_python_procedure',
        snowflake_conn_id='snowflake_con',  # Connection ID defined in Airflow
        sql="CALL USERS_LOAD_FROM_STAGE_TABLE();",
    )
