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

with DAG('DAG_airflow_shell_job_demo', default_args=default_args, schedule_interval=timedelta(seconds=45)) as dag:

    start_dag = DummyOperator(task_id='START_dag')
    shell_job1= BashOperator(
        task_id='shell_job1',
        # https://stackoverflow.com/questions/42147514/templatenotfound-error-when-running-simple-airflow-bashoperator
        bash_command= 'bash ' +  srcDir + 'list_all_files.sh ',
        dag=dag)
    shell_job2= BashOperator(
        task_id='shell_job2',
        bash_command='bash '  + srcDir + 'get_airflow_job_dag.sh ',
        dag=dag)
    end_dag = DummyOperator(task_id='END_dag')

    start_dag >> shell_job1 >> shell_job2 >> end_dag

