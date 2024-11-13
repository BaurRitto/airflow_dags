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
    dag_id='snowflake_users_posts_from_raw',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False
) as dag:
    
    # Task 1: Copy raw data from the stage (e.g., external stage) into a staging table
    sf_copy_into_raw = SnowflakeOperator(
        task_id='call_procedure_copy_into_raw_data',
        snowflake_conn_id='snowflake_con',  # Connection ID defined in Airflow
        sql="CALL copy_instagram_posts_raw('{{ params.start_date }}');",
        params={
            'start_date': '1999-99-99'
        }
    )

     # Task 2: Perform data transformation or cleaning on the staging table
    sf_copy_from_raw_to_prod = SnowflakeOperator(
        task_id='from_stage_table_to_prod_table',
        snowflake_conn_id='snowflake_con',
        sql="call insert_from_instagram_posts_raw();"
    )

    trancate_raw = SnowflakeOperator(
        task_id='from_stage_table_to_prod_table',
        snowflake_conn_id='snowflake_con',
        sql="truncate INSTAGRAM_POSTS_RAW;"
    )

    sf_copy_into_raw >> sf_copy_from_raw_to_prod >> trancate_raw

