from datetime import datetime

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator


from cosmos import DbtTaskGroup, ProjectConfig

from include.profiles import airflow_db
from include.constants import northwind_ex1_path, venv_execution_config
from airflow.operators.bash import BashOperator

@dag(
    schedule_interval="@quarterly",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["simple"],
)
def simple_task_group_ex1() -> None:
    """
    The simplest example of using Cosmos to render a dbt project as a TaskGroup.
    """
    seed_task = BashOperator(
        task_id='seed_data',
        bash_command='dbt seed',
    )

    northwind_ex1 = DbtTaskGroup(
        group_id="northwind_ex1_project",
        project_config=ProjectConfig(northwind_ex1_path),
        profile_config=airflow_db,
        execution_config=venv_execution_config,
    )

    post_dbt = EmptyOperator(task_id="post_dbt")

    seed_task >> northwind_ex1 >> post_dbt


simple_task_group_ex1()
