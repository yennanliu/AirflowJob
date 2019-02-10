from airflow.hooks.base_hook import BaseHook

class SlackHook(BaseHook):

    def __init__(self, slack_conn_id='slack_default'):
        self.slack_conn_id = slack_conn_id
        self.slack_conn = self.get_connection(slack_conn_id)
        self.token = self.slack_conn.token

    def get_conn(self):
        return self.token