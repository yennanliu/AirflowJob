from airflow import DAG
from airflow.operators.python_operator       import PythonOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 3, 1, 0, 0),
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
    'provide_context' : True # https://stackoverflow.com/questions/52541911/keyerror-ti-in-apache-airflow-xcom
}

dag = DAG('test_xcom_2',
    default_args = default_args)

def get_list():
    print ("*** get_list run")
    return [{'id':'001'}, {'id' : '002'}]

def parse_1(**kwargs):
    ti = kwargs['ti']
    # get listOfDict
    v1 = ti.xcom_pull(key=None, task_ids='get_lists')
    print("*** v1 = " + str(v1))

def parse_2(**kwargs):
    ti = kwargs['ti']
    # get listOfDict
    v1 = ti.xcom_pull(key=None, task_ids='get_lists')
    print("*** v1 = " + str(v1))

for data in get_list():
    sub_task1 = PythonOperator(
        task_id='data_parse1' + data['id'],
        python_callable=parse_1,
        op_kwargs={'dataObject': data},
        dag=dag,
     )

    sub_task2 = PythonOperator(
        task_id='data_parse2' + data['id'],
        python_callable=parse_2,
        op_kwargs={'dataObject': data},
        dag=dag,
     )
    sub_task1 >> sub_task2
