from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
import os

#################################################################
# DAG DEMO RUN SAPRK SCRIPT IN AIRFLOW ETL FRAMEWORK    
#################################################################

# ref 
# https://blog.insightdatascience.com/scheduling-spark-jobs-with-airflow-4c66f3144660
# https://github.com/danielblazevski/airflow-pyspark-reddit


srcDir = os.getcwd() + '/src/'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2016, 10, 14, 16, 12),
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
}

with DAG('airflowsparkdemo', default_args=default_args, schedule_interval=timedelta(seconds=45)) as dag:

    start_dag = DummyOperator(task_id='START_dag')
    spark_job= BashOperator(
        task_id='spark-job-run',
        bash_command='python ' + srcDir + 'pyspark_demo.py ',
        dag=dag)
    end_dag = DummyOperator(task_id='END_dag')

    start_dag >> spark_job >> end_dag

