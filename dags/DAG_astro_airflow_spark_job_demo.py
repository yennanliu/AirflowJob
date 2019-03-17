from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from datetime import datetime, timedelta
import os
import sys 
#from src import Spark_ML_RandomForestClassifier_titanic_demo 

#################################################################
# DAG DEMO RUN SAPRK SCRIPT IN AIRFLOW ETL FRAMEWORK    
#################################################################

# ref 
# https://blog.insightdatascience.com/scheduling-spark-jobs-with-airflow-4c66f3144660
# https://github.com/danielblazevski/airflow-pyspark-reddit

os.environ['SPARK_HOME'] = '/usr/local/airflow/'
sys.path.append(os.environ['SPARK_HOME'])

#srcDir = os.getcwd() + '/src/'
#srcDir = '/usr/local/airflow/dags/src/'
srcDir = os.getcwd() + 'dags/src/'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 1, 16, 12),
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
}

# env = {
#     #'SPARK_HOME': '/spark',
#     #'AIRFLOW_HOME' : '/usr/local/airflow/dags/'
#     #'JAVA_HOME': '/usr/bin' 
# }

with DAG('DAG_astro_airflow_spark_job_demo', default_args=default_args, schedule_interval=timedelta(seconds=45)) as dag:

    start_dag = DummyOperator(task_id='START_dag')

    print_path_env_task = BashOperator(
        task_id='print_path_env',
        bash_command='echo $PATH',
        dag=dag)

    print_ls_task = BashOperator(
        task_id='print_ls_task',
        bash_command='ls',
        dag=dag)

    export_spark_home_task = BashOperator(
        task_id='export_spark_home',
        bash_command='export SPARK_HOME=spark',
        dag=dag)

    spark_job= BashOperator(
        #env=env,
        task_id='spark-job-run',
        #bash_command= 'pwd' + 'ls' + 'ls tmp ' +  'python ' + srcDir + 'pyspark_demo.py ',
        #bash_command= 'pwd && ls && ls /tmp',
        bash_command='export HOME="$(cd ~ && pwd)" && export JAVA_HOME=/usr/bin  && export SPARK_HOME=/spark && echo $HOME $JAVA_HOME $SPARK_HOME && cd  && spark-submit ' + srcDir  + 'pyspark_demo.py ',
        dag=dag)
    spark_ml_job= BashOperator(
        task_id='spark-ml_job-run',
        bash_command='python ' + srcDir +  'Spark_ML_RandomForestClassifier_titanic_demo.py ',
        dag=dag)
    end_dag = DummyOperator(task_id='END_dag')

    start_dag >> print_path_env_task >>  print_ls_task >> export_spark_home_task  >> spark_job >> spark_ml_job >> end_dag

