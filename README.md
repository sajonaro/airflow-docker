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