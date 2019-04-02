# python 3 
import yaml
import os
import sqlite3


#################################################################
# DELETE DAG JOB RUN LOG/INSTANCE/ SQLITE (AIRFLOW BACKEND)
#################################################################


def truncate_airflow_table(cursor,tablename):
    sql = """
        DELETE FROM "{}"
    """
    cursor.execute(sql.format(tablename))

def main(db_file):
    to_truncate_tables = ['job',
                          'log',
                          'task_instance',
                          'task_fail',
                          'dag_stats',
                          'import_error',
                          'known_event']
    # config 
    conn = sqlite3.connect(db_file)
    for table in to_truncate_tables:
        try: 
            cursor = conn.cursor()
            print("Truncate airflow table : {}".format(table))
            truncate_airflow_table(cursor,table)
            conn.commit()

        except Exception as e:
            print ('Truncate table failed.. ')
            print (e)

if __name__ == '__main__':
    main('airflow.db')
