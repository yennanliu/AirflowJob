# OP
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator 
from airflow.operators.slack_operator import SlackAPIPostOperator
from datetime import datetime, timedelta
import pandas as pd 
import urllib 
import sys, os 


# UDF 
#sys.path.append("..") 
#os.system("export PYTHONPATH=$(pwd)")
from dags.utility.load_creds import *


# -------------- config --------------
# get exchangerates :  GBP -> USD 
url='https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01&base=GBP&symbols=USD'
SLACK_API_TOKEN = get_slack_api_secret()
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
	return content 


# airflow DAG 
args = {
    'owner': 'yen',
    'depends_on_past': False,
    'start_date': datetime(2018, 11, 6),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    }


slack_attachments = [
    {
        "color": "#342f54",
        "title": "GBP->USD EXCHANGE RATE",
        "footer": "Thanks!",
        "df_url": "{{ task_instance.xcom_pull(task_ids='get_api_data_step') }}",
    }
]


with DAG(dag_id='DAG_get_GBP_USD_exchange_rate', default_args=args) as dag:

	start_dag = DummyOperator(task_id='START_dag')

	get_api_data_step = PythonOperator(
	task_id='get_api_data_step',
	python_callable=get_exchange_rates_data)


	post_to_slack_step = SlackAPIPostOperator( 
	task_id = 'post_to_slack_step',
	channel= 'slack-bot-dev1',
	token = SLACK_API_TOKEN,
	username = 'Xbot', 
	text = """ 
			```
			id,vendor_id,passenger_count,pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude,trip_duration
			id2875421,2,1,-73.98215484619139,40.76793670654297,-73.96463012695312,40.765602111816406,455
			id2377394,1,1,-73.98041534423827,40.738563537597656,-73.99948120117188,40.73115158081055,663
			id3858529,2,1,-73.97902679443358,40.763938903808594,-74.00533294677734,40.71008682250977,2124
			id3504673,2,1,-74.01004028320312,40.719970703125,-74.01226806640625,40.70671844482422,429

           ```      	
		   """,
	attachments=slack_attachments)

	end_dag = DummyOperator(task_id='END_dag')

	start_dag >> get_api_data_step  >> post_to_slack_step >> end_dag



