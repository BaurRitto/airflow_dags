'''
Runs call procedure from snowflake
'''


from datetime import timedelta
from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'data_engineer',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='my_dag_id',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False
) as dag:
    # Call the stored procedure in Snowflake
    call_snowflake_procedure = SnowflakeOperator(
        task_id='call procedure copy into raw data',
        snowflake_conn_id='snowflake_con',  # Connection ID defined in Airflow
        sql="CALL copy_instagram_posts_raw('{{ params.start_date }}');",
        params={
            'start_date': '1999-99-99'
        }
    )
