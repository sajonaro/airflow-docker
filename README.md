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
* to start up the stack
  ```bash
  $ ./start.sh
  ```
  ... which does following  
    ```bash
    $ docker compose up airflow-init  
    $ sleep 5
    $ docker compose up   
    ```

* to use dbt cli use dbt commands [e.g init, run, seed, test ]:
  ```bash
  #use dbt commands [e.g init, run, seed, test ]
  # and then follow command prompts 
  $ docker compose run --rm dbt init
  ```  
   
### some useful commands
* if on linux 
  ```bash
  #create directories
  $ mkdir ./dags ./logs ./plugins ./dbt
  #configure UID and GID
  $ echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
  ``` 