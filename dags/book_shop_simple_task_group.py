from datetime import datetime

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator


from cosmos import DbtTaskGroup, ProjectConfig

from include.profiles import airflow_db
from include.constants import book_shop_path, venv_execution_config


@dag(
    schedule_interval="@quarterly",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["simple"],
)
def simple_task_group() -> None:
    """
    The simplest example of using Cosmos to render a dbt project as a TaskGroup.
    """
    pre_dbt = EmptyOperator(task_id="pre_dbt")

    book_shop = DbtTaskGroup(
        group_id="my_book_shop_project",
        project_config=ProjectConfig(book_shop_path),
        profile_config=airflow_db,
        execution_config=venv_execution_config,
    )

    post_dbt = EmptyOperator(task_id="post_dbt")

    pre_dbt >> book_shop >> post_dbt


simple_task_group()
