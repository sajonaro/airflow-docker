"Contains constants used in the DAGs"

from pathlib import Path
from cosmos import ExecutionConfig

book_shop_path = Path("/opt/airflow/dbt/projects/books_shop_example")
dbt_executable = Path("/opt/airflow/dbt_venv/bin/dbt")

venv_execution_config = ExecutionConfig(
    dbt_executable_path=str(dbt_executable),
)
