from airflow import DAG
from airflow.operators.python_operator       import PythonOperator
from airflow.operators.dummy_operator        import DummyOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta

value_1 = [1, 2, 3]
value_2 = {'a': 'b'}


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 3, 1, 0, 0),
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
    'provide_context' : True # https://stackoverflow.com/questions/52541911/keyerror-ti-in-apache-airflow-xcom
}

dag = DAG('test_xcom_3',
    default_args = default_args)

def push1(**kwargs):
    """Pushes an XCom without a specific target"""
    kwargs['ti'].xcom_push(key='value from pusher 1', value=value_1)


def push2(**kwargs):
    """Pushes an XCom without a specific target, just by returning it"""
    return value_2


def pull1(**kwargs):
    ti = kwargs['ti']
    #pulled_value_1 = ti.xcom_pull(key=None, task_ids='push')
    #pulled_value_1 = ti.xcom_pull(key='value from pusher 1', task_ids='push')
    
    ### NOTICE : WE NEED SET task_ids='push1' THEN CAN GET RETURN VALUES FROM "push1" py method
    pulled_value_1 = ti.xcom_pull(key=None, task_ids='push1') 
    print ("*** pulled_value_1 = " + str(pulled_value_1))


def pull2(**kwargs):
    ti = kwargs['ti']
    pulled_value_2 = ti.xcom_pull(task_ids='push2')
    print ("*** pulled_value_2 = " + str(pulled_value_2))


push1 = PythonOperator(
    task_id='push1',
    python_callable=push1,
    dag = dag
)

push2 = PythonOperator(
    task_id='push2',
    python_callable=push2,
    dag = dag
)

pull1 = PythonOperator(
    task_id='pull1',
    python_callable=pull1,
    dag = dag
)

pull2 = PythonOperator(
    task_id='pull2',
    python_callable=pull2,
    dag = dag
)

end = DummyOperator(task_id = 'end', retries = 0, dag=dag)


push1 >> pull1 >> end
push2 >> pull2 >> end
