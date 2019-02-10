
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator 
from datetime import datetime, timedelta
import os 
from plugins.hooks.insta_hook import InstagramHook

# help func 
def IG_demo_job():
	from instapy import InstaPy
	from instapy.util import smart_run
	insta_username, insta_password = InstagramHook().get_conn()
	# get an InstaPy session!
	# set headless_browser=True to run InstaPy in the background
	session = InstaPy(username=insta_username,
	                  password=insta_password,
	                  headless_browser=False)
	with smart_run(session):
	    """ Activity flow """
	    # settings
	    session.set_relationship_bounds(enabled=True,
	                                    delimit_by_numbers=True,
	                                    max_followers=4590,
	                                    min_followers=45,
	                                    min_following=77)
	    session.set_dont_include(["friend1", "friend2", "friend3"])
	    session.set_dont_like(["pizza", "#store"])
	    # actions
	    session.like_by_tags(["natgeo"], amount=10)

# airflow DAG 
args = {
    'owner': 'yen',
    'depends_on_past': False,
    'start_date': datetime(2018, 11, 6),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    }


with DAG(dag_id='DAG_IG_bot_job_demo', default_args=args) as dag:

	start_dag = DummyOperator(task_id='START_dag')

	IG_bot_job = PythonOperator(
	task_id='IG_bot_job',
	python_callable=IG_demo_job)

	end_dag = DummyOperator(task_id='END_dag')

	start_dag >> IG_bot_job >> end_dag
