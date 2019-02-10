
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator 
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime, timedelta
import os 
# UDF 

#----------------------------------------------------
# config 

# try:
#     access_token, access_token_secret, consumer_key, consumer_secret = get_twitter_api_secret() 
#     APP_KEY=consumer_key
#     APP_SECRET=consumer_secret

# except:
#     access_token = os.environ['access_token']
#     access_token_secret = os.environ['access_token_secret']
#     consumer_key = os.environ['consumer_key']
#     consumer_secret = os.environ['consumer_secret'] 
# else:
#     print (' No API key , please set up  via : ')
#     print (' https://developer.twitter.com/en/apps')

#----------------------------------------------------
# OP 

def update2sqlite(df):
    try:
        df_ = df 
        engine = create_engine('sqlite:///twitter_data.db', echo=False)
        df_.to_sql('twitter_data',if_exists='replace',con=engine)
        print ('update to DB ok')
    except:
        print ('dump DB failed')

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (data)


def get_twitter_data():
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
#----------------------------------------------------
# DAG 

args = { 'owner': 'yen',
    'depends_on_past': False,
    'start_date': datetime.now()}

dag = DAG('DAG_twitter_batch_job_demo', default_args=args)

get_twitter_stream_data_task = PythonOperator(
    task_id='get_twitter_stream_data_part',
    python_callable = get_twitter_data,
    dag=dag
    )
save_to_db_task = PythonOperator(
    task_id='sqlite_IO',
    python_callable=update2sqlite
    )

# define workflow
#get_twitter_stream_data_task >>  save_to_db_task
get_twitter_stream_data_task
