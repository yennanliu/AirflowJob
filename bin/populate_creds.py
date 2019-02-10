

#################################################################
# POPULATE CREDS TOO LOCAL POSTGRESQL (AIRFLOW BACKEND)
#################################################################

# python 3 
import yaml
import os
import psycopg2


with open('../.creds.yml') as f:
    config = yaml.load(f)


SLACK_API_TOKEN = config['slack_api']['token']

def get_slack_api_secret():
	print (' slack_api_token = ', slack_api_token)
	return slack_api_token

def insert_slack_default_conn(cursor):
    sql = """
        INSERT INTO public."connection"
        (conn_id, conn_type, host, "schema", login, password, port, extra, is_encrypted, is_extra_encrypted)
        VALUES('slack_default', 'slack', '', '', '{DEFAULT_SLACK_API_TOKEN}', '{DEFAULT_SLACK_API_TOKEN}', 0, '', false, false);
        """.format(
            DEFAULT_SLACK_API_TOKEN=SLACK_API_TOKEN,
            DEFAULT_SLACK_API_TOKEN2=SLACK_API_TOKEN
            )
    cursor.execute(sql)

def insert_datadog_default_conn(cursor):
    sql = """
        INSERT INTO public."connection"
        (conn_id, conn_type, host, "schema", login, password, port, extra, is_encrypted, is_extra_encrypted)
        VALUES('datadog_default', '', '', '', '{DATADOG_LOGIN}', '{DATADOG_PASSWORD}', 0, '', false, false);
        """.format(
            DATADOG_LOGIN=DATADOG_LOGIN,
            DATADOG_PASSWORD=DATADOG_PASSWORD
    )

    cursor.execute(sql)

def main():
    # config 
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='postgres'"
    conn = psycopg2.connect(conn_string)
    conn.autocommit = True
    try: 
        cursor = conn.cursor()
        print('Inserting slack credentials')
        insert_slack_default_conn(cursor)
    except Exception as e:
        print ('Insert credentials failed.. ')
        print (e)


if __name__ == '__main__':
    main()


