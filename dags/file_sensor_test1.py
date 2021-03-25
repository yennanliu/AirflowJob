from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.dummy_operator    import DummyOperator

from datetime import datetime, timedelta
import airflow

# https://stackoverflow.com/questions/54791596/any-example-of-airflow-filesensor/54804112
# https://airflow.apache.org/code.html#airflow.models.BaseOperator

default_args = {
    "depends_on_past" : False,
    'start_date': datetime(2021, 2, 1, 0),
    'end_date': datetime(2021, 2, 28, 0),
    "retries"         : 1,
    'retry_delay': timedelta(minutes=1),
}

with airflow.DAG( "file_sensor_test1", default_args= default_args) as dag:

    start_task  = DummyOperator(  task_id= "start" )
    stop_task   = DummyOperator(  task_id= "stop"  )
    sensor_task = FileSensor( task_id= "file_sensor_test1", poke_interval= 30, filepath= 'dara/xxx.csv' )

start_task >> sensor_task >> stop_task
