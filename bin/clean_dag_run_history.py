# python 3 
import yaml
import os
import psycopg2

#################################################################
# DELETE DAG JOB RUN LOG/INSTANCE/ POSTGRE (AIRFLOW BACKEND)
#################################################################


def truncate_airflow_table(cursor,tablename):
    sql = """
        TRUNCATE TABLE public."{}"
    """
    cursor.execute(sql.format(tablename))

def main():
    # config 
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='postgres'"
    conn = psycopg2.connect(conn_string)
    conn.autocommit = True
    to_truncate_tables = ['job',
                          'log',
                          'task_instance',
                          'task_fail',
                          'dag_stats',
                          'dag_run',
                          'import_error',
                          'known_event',
                          'variable',
                          'xcom']
    for table in to_truncate_tables:
      try: 
          cursor = conn.cursor()
          print("Truncate airflow table : {}".format(table))
          truncate_airflow_table(cursor,table)
      except Exception as e:
          print ('Truncate table failed.. ')
          print (e)


if __name__ == '__main__':
    main()
