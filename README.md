## About

This is a small PoC demonstrating use of airflow + Dbt+ cosmos in docker 

[Dbt](https://www.getdbt.com/) provides:
  - well structured transformation pipeline
      * model first approach: i.e. each transformation step is defined as 'model'
  - testing
  - version control
  - modularization & centralization of (analytics) code

  
[Cosmos](https://www.astronomer.io/cosmos/) provides:
  - automatic conversion of Dbt projects into DAGs
  - dependency visualization
  - ability to run any number of Dbt jobs (virtually for free as there is dependency on Dbt core only)

[Airflow](https://airflow.apache.org/) provides:
  - extensible automation/orchestrating platform to run Dbt steps as [DAGs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#dags)
  - web ui
  - cli 
  - ..and more

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

* to use dbt cli (via docker compose):
  ```bash
  # use dbt commands [e.g init, run, seed, test ]
  # and then follow command prompts 
  $ docker compose run --rm dbt-cli dbt init
  ```  
  .. or alternatively (via virtual environment)
  ```bash
  # 1 - create virtual environment = dbt  
  # 2 - activate it 
  # 3 - install dbt libs

  $ python3 -m venv dbt \
    && source dbt/bin/activate \
    && pip install dbt-core dbt-postgres \
    && deactivate
  ```
   


### some useful commands
* use postgres cli
  ```bash
    # attach to db container as root
    # then connect to database e.g. 
    #     user = airflow,  db = ex1, port = 5454
    $ psql -U airflow -h localhost ex1 -p 5454

    # 'out' is the schema name
    SELECT * FROM pg_catalog.pg_tables WHERE schemaname='out';

    # assuming there is table `customers` in schema `out`
    SELECT * from out.customers;
  ```

* if on linux 

  ```bash
    #create directories
    $ mkdir ./dags ./logs ./plugins ./dbt
    #configure UID and GID
    $ echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
  ``` 