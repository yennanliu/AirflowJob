from airflow import DAG
from airflow.operators.python_operator       import PythonOperator
from airflow.operators.dummy_operator        import DummyOperator
from airflow.operators.bash_operator       import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 3, 1, 0, 0),
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
    'provide_context' : True # https://stackoverflow.com/questions/52541911/keyerror-ti-in-apache-airflow-xcom
}

dag = DAG('test_xcom_6',
    default_args = default_args)

def pull1(**kwargs):
    ti = kwargs['ti']
    pulled_value_1 = ti.xcom_pull(key=None, task_ids='push1')
    print ("*** pulled_value_1 = " + str(pulled_value_1))

bash_cmd="""data="`cat test.txt`" && echo $data"""

push1 = SSHOperator(
    task_id='push1',
    command=bash_cmd,
    ssh_conn_id = 'user@some_server',
    do_xcom_push=True, # https://airflow.apache.org/docs/apache-airflow/1.10.12/_modules/airflow/contrib/operators/ssh_operator.html
    dag=dag)

pull1 = BashOperator(
    task_id='pull1',
    bash_command="echo {{ ti.xcom_pull(task_ids='push1') }}",
    xcom_push=True,
    dag=dag)

end = DummyOperator(task_id = 'end', retries = 0, dag=dag)


push1 >> pull1 >> end
