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


os.environ['SPARK_HOME'] = '/spark'

#srcDir = os.getcwd() + '/src/'
srcDir = '/dags/src/'


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 1, 16, 12),
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
}


with DAG('airflowsparkdemo', default_args=default_args, schedule_interval=timedelta(seconds=45)) as dag:

    start_dag = DummyOperator(task_id='START_dag')

    print_path_env_task = BashOperator(
        task_id='print_path_env',
        bash_command='echo $PATH',
        dag=dag)

    spark_job= BashOperator(
        task_id='spark-job-run',
        #bash_command= 'pwd' + 'ls' + 'ls tmp ' +  'python ' + srcDir + 'pyspark_demo.py ',
        bash_command= 'pwd && ls && ls /tmp/airflowtmphvku3n3v',
        dag=dag)
    spark_ml_job= BashOperator(
        task_id='spark-ml_job-run',
        bash_command='python ' + srcDir + 'Spark_ML_LinearRegression_demo.py ',
        dag=dag)
    end_dag = DummyOperator(task_id='END_dag')

    start_dag >> print_path_env_task >> spark_job >> spark_ml_job >> end_dag


