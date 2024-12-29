from airflow import DAG # type: ignore
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'retries': 1,
}

with DAG(
    dag_id='test_dag_v2',
    default_args=default_args,
    description='Test DAG', 
    start_date=datetime(2021, 1, 1),
    schedule_interval='@daily'
) as dag:
    task1=BashOperator(
        task_id='task1',
        bash_command='echo "Hello World!"'
    )

    task2=BashOperator(
        task_id='task2',
        bash_command='echo "Hello from task 2"'
    )
    
    task1.set_downstream(task2)