"Contains profile mappings used in the project"

from cosmos import ProfileConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping


ex1_db = ProfileConfig(
    profile_name="ex1",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="ex1",
        profile_args={"schema": "out"},
    ),
)

ex2_db = ProfileConfig(
    profile_name="ex2",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="ex2",
        profile_args={"schema": "out"},
    ),
)

airflow_db = ProfileConfig(
    profile_name="bookshop",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="bookshop_con",
        profile_args={"schema": "out"},
    ),
)
