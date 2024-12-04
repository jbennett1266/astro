from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def print_hello():
    print("Hello World!")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 11, 30),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'hello_world_dag',
    default_args=default_args,
    description='A simple DAG that prints Hello World',
    schedule_interval=timedelta(days=1),
) as dag:

    task1 = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello,
    )
