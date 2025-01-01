FROM apache/airflow:2.10.4-python3.8

RUN apt update && \
    apt install -y --no-install-recommends \
    mc

# install dbt into a virtual environment
RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-postgres==1.8.2 && deactivate

# set a connection to the airflow metadata db to use for testing
# ENV AIRFLOW_CONN_AIRFLOW_METADATA_DB=postgresql+psycopg2://postgres:postgres@postgres:5432/postgres
