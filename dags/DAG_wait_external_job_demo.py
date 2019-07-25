from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.sensors import ExternalTaskSensor

def run_after_external_job():
    print ('this is job running after external steps')
 
args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2016, 10, 14, 16, 12),
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'DAG_wait_external_job_demo',
    description='demo DAG depends external upstream',
    schedule_interval='0 7 * * *',
    start_date=datetime(2018, 10, 17),
    catchup=True,
    default_args=args,
)

start_dag = DummyOperator(task_id='START_dag')

after_run_operator = PythonOperator(task_id='after_external_run_step', python_callable=run_after_external_job, dag=dag)

end_dag = DummyOperator(task_id='END_dag')

source = DummyOperator(task_id='source', dag=dag)

dep_dags = ['hello_world_dag']

for dep_dag in dep_dags:

    task_id = 'external_task_sensor_{}'.format(dep_dag)

    sensor = ExternalTaskSensor(
    external_dag_id=dep_dag,
    external_task_id='end_dag_{}'.format(dep_dag),
    task_id=task_id,
    execution_delta=timedelta(minutes=5), 
    dag=dag
    )

    sensor >> source # add external job depedency  

source >> start_dag >> after_run_operator >> end_dag  # only run this DAG after external job (DAG) completed 
