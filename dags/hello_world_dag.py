from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
	return 'Hello Wolrd'

 args = {
		'owner': 'yen',
		'depends_on_past': False,
		'start_date': datetime(2018, 12, 30),
		'retries': 1,
		'retry_delay': timedelta(minutes=1),
		'provide_context':True
		}

with DAG(dag_id='hello_world_dag', 
		 default_args=args) as dag:

	start_dag = DummyOperator(task_id='START_dag')

	hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

	end_dag = DummyOperator(task_id='END_dag')

	start_dag >> hello_operator >> end_dag
