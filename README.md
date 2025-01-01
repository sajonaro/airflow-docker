## About

This is a small PoC demonstrating use of airflow + Dbt+ cosmos in docker 

[Dbt](https://www.getdbt.com/) provides:
  - testing
  - version control
  - modularization & centralization of (analytics) code
  - model first approach 
  
[Cosmos](https://www.astronomer.io/cosmos/) provides:
  - dependency visualization
  - observability

[Airflow](https://airflow.apache.org/) provides:
  - orchestrating platform to run Dbt steps as [DAGs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#dags)
  - web ui

## 101
* ```
  mkdir ./dags ./logs ./plugins 
  ``` 
  if on linux 
  ```
  echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
  ```

* init via command:
  ```
  docker compose up airflow-init  
  ```

* run via command:
  ```
  docker compose up   
  ```  

* use dbt commands [e.g init, run, seed, test ]:
  ```
    docker compose run --rm dbt init
  ```  
  and then follow command prompts   
