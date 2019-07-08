from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
import os

srcDir = os.getcwd() + '/dags/src/'
CLASSPATH = "/Users/yennanliu/XJob/dags/src:.:/Users/$USER/spark/jars/*"

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2016, 10, 14, 16, 12),
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
}

with DAG('DAG_airflow_JAVA_spark_job_demo', default_args=default_args, schedule_interval=timedelta(seconds=45)) as dag:

    start_dag = DummyOperator(task_id='START_dag')
    java_spark_job1_compile= BashOperator(
        task_id='java-ml_job-compile',
        bash_command='javac -classpath ' + CLASSPATH +  ' {}Spark_java_BasicAvg_demo.java '.format(srcDir),
        dag=dag)
    java_spark_job1_run= BashOperator(
        task_id='java_ml_job-run',
        bash_command='java  -classpath ' + CLASSPATH +  ' Spark_java_BasicAvg_demo ',
        dag=dag)
    end_dag = DummyOperator(task_id='END_dag')

    start_dag >> java_spark_job1_compile >> java_spark_job1_run >> end_dag

