from airflow import DAG
from airflow.operators.dummy_operator        import DummyOperator
from airflow.operators.python_operator       import PythonOperator
from airflow.contrib.operators.ssh_operator  import SSHOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.trigger_rule              import TriggerRule
from datetime                                import datetime, timedelta
from time                                    import time, sleep

base_cmd = "bash ../script/must_failed.py"


dag = DAG('DAG_run_exit1_py_script',
           description='must failed',
           start_date=datetime(2021, 4, 1, 0),
           schedule_interval='@daily',
           max_active_runs= 3,
           catchup=True)


run_must_failed = BashOperator(task_id = 'run_must_failed'
                     ,bash_command = base_cmd
                     ,retries = 3
                     ,pool = 'default_pool'
                     ,dag = dag)

start = DummyOperator(task_id = 'start', retries = 0, pool = 'default_pool', dag=dag)
end = DummyOperator(task_id = 'end', retries = 0, pool = 'default_pool', dag=dag)

start >> run_must_failed >> end