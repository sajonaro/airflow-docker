"""
An example DAG that uses Cosmos to render a dbt project.
"""

import os
from datetime import datetime
from pathlib import Path

from cosmos import DbtDag, ProjectConfig, ProfileConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping

from include.profiles import ex2_db
from include.constants import northwind_ex2_path, venv_execution_config


DEFAULT_DBT_ROOT_PATH = Path(__file__).parent.parent / "dbt/projects"
DBT_ROOT_PATH = Path(os.getenv("DBT_ROOT_PATH", DEFAULT_DBT_ROOT_PATH))

# [START local_example]
northwind_ex2_basic_cosmos_dag = DbtDag(
    # dbt/cosmos-specific parameters
    project_config=ProjectConfig(northwind_ex2_path),
    profile_config=ex2_db,
    execution_config=venv_execution_config,
    operator_args={
        "install_deps": True,  # install any necessary dependencies before running any dbt command
        "full_refresh": True,  # used only in dbt commands that support this flag
    },
    # normal dag parameters
    schedule_interval="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    dag_id="northwind_ex2_basic_cosmos_dag",
    default_args={"retries": 2},
)
# [END local_example]