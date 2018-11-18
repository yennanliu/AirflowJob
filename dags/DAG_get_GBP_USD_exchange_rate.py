# OP
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator 
from airflow.operators.slack_operator import SlackAPIPostOperator
from datetime import datetime, timedelta
import pandas as pd 
import urllib 


# -------------- config --------------
# get exchangerates :  GBP -> USD 
url='https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01&base=GBP&symbols=USD'
# -------------- config --------------


# help func 
def get_country_name(country_name_rates):
    return list(country_name_rates.keys())[0]

def get_country_rate(country_name_rates): 
    return float((list(country_name_rates.values()))[0])

def get_exchange_rates_data():
	content = urllib.request.urlopen(url).read()
	df=pd.read_json(content)
	df['country_name']= df['rates'].map(get_country_name)
	df['country_rate']= df['rates'].map(get_country_rate)
	print (' API response (df):', df.head())
	return df 


# airflow DAG 
args = {
    'owner': 'yen',
    'depends_on_past': False,
    'start_date': datetime(2018, 11, 6),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    }


with DAG(dag_id='DAG_get_GBP_USD_exchange_rate', default_args=args) as dag:

	start_dag = DummyOperator(task_id='START_dag')

	get_api_data_step = PythonOperator(
	task_id='get_api_data_step',
	python_callable=get_exchange_rates_data)

	post_to_slack_step = SlackAPIPostOperator( 
	task_id = 'post_to_slack_step',
	channel= SLACK_CHANNEL,
	token = SLACK_TOKEN,
	username = SLACK_USER, 
	text = 'this is a msg from XBbot slack bot')

	end_dag = DummyOperator(task_id='END_dag')

	start_dag >> get_api_data_step >> post_to_slack_step >> end_dag



