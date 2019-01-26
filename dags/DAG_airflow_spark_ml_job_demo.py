from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
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

with DAG('DAG_airflow_spark_ml_job_demo', default_args=default_args, schedule_interval=timedelta(seconds=45)) as dag:

    start_dag = DummyOperator(task_id='START_dag')
    spark_ml_job_1= BashOperator(
        task_id='spark-ml_job1-run',
        bash_command='spark-submit ' + srcDir + 'Spark_ML_RandomForestClassifier_titanic_demo.py ',
        dag=dag)
    spark_ml_job_2= BashOperator(
        task_id='spark-ml_job2-run',
        bash_command='python ' + srcDir + 'Spark_ML_LinearRegression_demo.py ',
        dag=dag)
    end_dag = DummyOperator(task_id='END_dag')

    start_dag >> spark_ml_job_1 >> spark_ml_job_2 >> end_dag

