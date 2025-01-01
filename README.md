# 101
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
