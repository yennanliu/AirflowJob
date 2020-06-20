from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
import os

srcDir = os.getcwd() + '/dags/src/'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2016, 10, 14, 16, 12),
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
}

with DAG('DAG_airflow_JAVA_job_demo', default_args=default_args, schedule_interval=timedelta(seconds=45)) as dag:

    start_dag = DummyOperator(task_id='START_dag')
    java_job1_compile= BashOperator(
        task_id='java-job-compile',
        bash_command='javac ' + srcDir + 'HelloWorld.java ',
        dag=dag)
    java_job1_run= BashOperator(
        task_id='java_job-run',
        bash_command='java  -classpath ' + srcDir + ' HelloWorld ',
        dag=dag)
    end_dag = DummyOperator(task_id='END_dag')

    start_dag >> java_job1_compile >> java_job1_run >> end_dag
