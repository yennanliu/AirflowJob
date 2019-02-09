### Quick Start (Airflow)

- Please run the following commands step by step, then the airflow server should be able to run local
- Access the UI : http://localhost:8088  

```bash
# STEP 0) install env 
git clone https://github.com/yennanliu/XBot && cd XBot
bash install_pyspark.sh 
# STEP 1) run the dev env and export SPARK_HOME
source activate pyspark_
export SPARK_HOME=/Users/$USER/spark
export PATH=$SPARK_HOME/bin:$PATH

# STEP 2) export AIRFLOW_HOME and set language as US.UTF-8 
export AIRFLOW_HOME=/Users/$USER/XBot
export PYTHONPATH=/Users/$USER/XBot
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
# STEP 3) init airflow webserver
### in the current termianl ###
airflow initdb
airflow webserver -p 8088

# STEP 4) init airflow scheduler
### OPEN UP THE OTHER NEW TERMINAL, RUN STEP 1) -> STEP 2), THEN RUN FOLLOWING COMMAND ### 
airflow scheduler
# STEP 5) access airflow UI
# http://localhost:8088
```