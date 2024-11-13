from datetime import timedelta
from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'data_engineer',
    # 'retries': 1,
    # 'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='snowflake_users_posts_from_raw',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False
) as dag:
    
    trancate_raw = SnowflakeOperator(
            task_id='from_stage_table_to_prod_table',
            snowflake_conn_id='snowflake_con',
            sql="truncate INSTAGRAM_POSTS_RAW;"
        )


