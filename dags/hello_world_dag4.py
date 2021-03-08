from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2016, 10, 14, 16, 12),
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
}


def print_hello():
    return 'Hello Wolrd'


start_dag = DummyOperator(task_id='START_dag')

end_dag1 = DummyOperator(task_id='END1_dag')

end_dag2 = DummyOperator(task_id='END2_dag')


hello_pattern = dict()


with DAG(dag_id='hello_world_dag4', 
    default_args=args,
    start_date=datetime(2021, 2, 1, 0)) as dag:

    list_ =  ["abc", "def", "ghi", "jkl", "xyz"]
     
    # hello_pattern["abc"] =   DummyOperator(task_id='abc')
    # hello_pattern["def"] =   DummyOperator(task_id='def')
    # hello_pattern["ghi"] =   DummyOperator(task_id='ghi')
    # hello_pattern["jkl"] =   DummyOperator(task_id='jkl')

    for i in range(len(list_)):
        cur_ = list_[i]
        hello_pattern[cur_] = DummyOperator(task_id='{}'.format(cur_))
    
    for i in range(len(list_) - 1):

        #hello_pattern["abc"] >> hello_pattern["def"] >> hello_pattern["ghi"]
        cur_ = list_[i]
        next_ = list_[i+1]
        hello_pattern[cur_] >> hello_pattern[next_]

    start_dag >> hello_pattern[list_[0]]
    hello_pattern[list_[-1]] >> end_dag1
    end_dag1 >> end_dag2
