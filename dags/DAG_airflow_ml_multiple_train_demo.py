from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
import os
import pandas as pd 

try:
    from sklearn import datasets
    from sklearn import tree 
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import confusion_matrix
    from sklearn.model_selection import cross_val_score
    from sklearn.metrics import classification_report
except:
    print (' NO ML packages')



srcDir = os.getcwd() + '/dags/src/'


# OP ---------------------------------------  
def train(df,model):
    df_ = df.copy()
    X = df_.iloc[:,1:4]
    y = df_.iloc[:,-1:]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    clf_ = model.fit(X_train, y_train)
    print ('test score :', model.score(X_test,y_test) )
    y_true = y_test
    y_pred = clf_.predict(X_test)
    print ('-------------------')
    print ('confusion matrix : ')
    print (confusion_matrix(y_true, y_pred))
    print ('-------------------')
    print ('classification report  : ')
    print (classification_report(y_true, y_pred))
    #print (clf_)
    return clf_
# OP ---------------------------------------  



def create_data():
    data =  datasets.load_iris()
    df= pd.DataFrame(data.data)
    df.columns = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width']
    df['class'] = data['target']
    df.to_csv('iris.csv',index=False)

def load_data_and_train():
    print ('----- STEP 1)  LOAD  DATA')
    df_iris = pd.read_csv('iris.csv')
    print ('----- STEP 2)  TRAIN/TEST SET SPLIT')
    print ('----- STEP 3)  TRAIN')
    clf_tree = tree.DecisionTreeClassifier()
    clf_tree_ = train(df_iris,clf_tree )
    print ('----- STEP 4)  TEST')


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2016, 10, 14, 16, 12),
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
}

with DAG('DAG_airflow_ml_multiple_train_demo', default_args=default_args, schedule_interval=timedelta(seconds=45)) as dag:

    start_dag = DummyOperator(task_id='START_dag')

    create_data_job= PythonOperator(
        task_id='create_data',
        python_callable=create_data, 
        dag=dag,
        args=default_args)

    end_dag = DummyOperator(task_id='END_dag')

    for i in range(10,20):

        load_data_and_train_job= PythonOperator(
            task_id='load_data_and_train{}'.format(i),
            python_callable=load_data_and_train,
            dag=dag,
            args=default_args)

        create_data_job >> load_data_and_train_job  >>  end_dag


    

    start_dag >> create_data_job 

