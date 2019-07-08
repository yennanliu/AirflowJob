# OP
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator 
#from airflow.operators.slack_operator import SlackAPIPostOperator
from datetime import datetime, timedelta
import pandas as pd 
import urllib 
import sys, os
import json 
#from plugins.hooks.slack_hook import SlackHook
# UDF 
#sys.path.append("..") 
#os.system("export PYTHONPATH=$(pwd)")
#from dags.utility.load_creds import *

# -------------- config --------------
# get exchangerates :  GBP -> USD 
url='https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01&base=GBP&symbols=USD'
# -------------- config --------------

# help func 
def get_country_name(country_name_rates):
    return list(country_name_rates.keys())[0]

def get_country_rate(country_name_rates): 
    return float((list(country_name_rates.values()))[0])

def fix_to_json(bytes_data):
	# fix bytes data to json make it's OK to parse in python 
	# https://stackoverflow.com/questions/40059654/python-convert-a-bytes-array-into-json-format
	return json.loads(bytes_data.decode('utf8').replace("'", '"'))

def get_exchange_rates_data(**kwargs):
	SLACK_API_TOKEN = SlackHook().get_conn()
	content = urllib.request.urlopen(url).read()
	content_ = fix_to_json(content)
	df=pd.read_json(content)
	df['country_name']= df['rates'].map(get_country_name)
	df['country_rate']= df['rates'].map(get_country_rate)
	print (' API response (df):', df.head())
	#return content
	kwargs['ti'].xcom_push(key='UK_USD_rates', value=content) 
	slack_attachments = [
	{
	"color": "#342f54",
	"title": "GBP->USD EXCHANGE RATE",
	"footer": 'OK',
	"df_url": "{{ task_instance.xcom_pull(task_ids='get_api_data_step') }}",
	} ]
	slack_post = SlackAPIPostOperator( 
	task_id = 'post_to_slack_step',
	channel= 'slack-bot-dev1',
	token = SLACK_API_TOKEN,
	username = 'XJob', 
	text = content_, 
	attachments=slack_attachments,
	provide_context=True)
	return slack_post.execute(content='123')

def post_to_slack(**kwargs):
	SLACK_API_TOKEN = SlackHook().get_conn()
	msg= kwargs['ti'].xcom_pull(key=None,task_ids='get_exchange_rates_data')
	print ('msg :' , msg)
	slack_attachments = [
    {
        "color": "#342f54",
        "title": "GBP->USD EXCHANGE RATE",
        "footer": kwargs['ti'].xcom_pull(key='UK_USD_rates', task_ids='get_exchange_rates_data'),
        "df_url": "{{ task_instance.xcom_pull(task_ids='get_api_data_step') }}",
    } ]
	slack_post = SlackAPIPostOperator( 
	task_id = 'post_to_slack_step',
	channel= 'slack-bot-dev1',
	token = SLACK_API_TOKEN,
	username = 'XJob', 
	text = kwargs['ti'].xcom_pull(key='UK_USD_rates',task_ids='get_exchange_rates_data'),
	attachments=slack_attachments,
	provide_context=True)
	return slack_post.execute(content='123')

# airflow DAG 
args = {
    'owner': 'yen',
    'depends_on_past': False,
    'start_date': datetime(2018, 12, 30),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'provide_context':True
    }

with DAG(dag_id='DAG_get_GBP_USD_exchange_rate', 
		 default_args=args) as dag:

	start_dag = DummyOperator(task_id='START_dag')

	get_api_data_step = PythonOperator(
	task_id='get_api_data_step',
	python_callable=get_exchange_rates_data,
	provide_context=True,
	dag=dag,
	args=args)

	post_to_slack_step = PythonOperator(
	task_id='post_to_slack_step',
	python_callable=post_to_slack,
	provide_context=True,
	dag=dag,
	args=args)

	end_dag = DummyOperator(task_id='END_dag')

	start_dag >> get_api_data_step  >> post_to_slack_step >> end_dag
