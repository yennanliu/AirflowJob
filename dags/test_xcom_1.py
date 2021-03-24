from airflow import DAG
from airflow.operators.python_operator       import PythonOperator
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

dag = DAG('test_xcom_1',
    default_args = default_args)

def push(**kwargs):
    """Pushes an XCom without a specific target"""
    kwargs['ti'].xcom_push(key='value from pusher 1', value=value_1)


def push_by_returning(**kwargs):
    """Pushes an XCom without a specific target, just by returning it"""
    return value_2


def puller(**kwargs):
    """Pull all previously pushed XComs and check if the pushed values match the pulled values."""
    ti = kwargs['ti']

    # get value_1
    pulled_value_1 = ti.xcom_pull(key=None, task_ids='push')
    if pulled_value_1 != value_1:
        raise ValueError(f'The two values differ {pulled_value_1} and {value_1}')

    # get value_2
    pulled_value_2 = ti.xcom_pull(task_ids='push_by_returning')
    if pulled_value_2 != value_2:
        raise ValueError(f'The two values differ {pulled_value_2} and {value_2}')

    # get both value_1 and value_2
    pulled_value_1, pulled_value_2 = ti.xcom_pull(key=None, task_ids=['push', 'push_by_returning'])
    if pulled_value_1 != value_1:
        raise ValueError(f'The two values differ {pulled_value_1} and {value_1}')
    if pulled_value_2 != value_2:
        raise ValueError(f'The two values differ {pulled_value_2} and {value_2}')


push1 = PythonOperator(
    task_id='push',
    python_callable=push,
    dag = dag
)

push2 = PythonOperator(
    task_id='push_by_returning',
    python_callable=push_by_returning,
    dag = dag
)

pull = PythonOperator(
    task_id='puller',
    python_callable=puller,
    dag = dag
)

pull << [push1, push2]

