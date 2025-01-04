#use airflow runtime
FROM apache/airflow:2.10.4-python3.8

# extending airflow image 
# per documentation here https://airflow.apache.org/docs/docker-stack/build.html#adding-a-new-pypi-package


#install mc as root (just for convenience)
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         mc \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow

#switch back to airflow user 
USER airflow
COPY --chown=airflow . .

# and install airflow-wide packages and 
RUN pip install --no-cache-dir astronomer-cosmos

# Install dbt in a virtual environment to ensure there are no conflicts with airflow packages
RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-postgres==1.8.2  && deactivate
