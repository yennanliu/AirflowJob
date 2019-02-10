from airflow.hooks.base_hook import BaseHook

class InstagramHook():

    def __init__(self, snowflake_conn_id='instagram'):
        self.instagram_conn_id = instagram_conn_id
        self.instagram_conn = self.get_connection(instagram_conn_id)
        self.insta_username = self.instagram_conn.login
        self.insta_password = self.instagram_conn.password

    def get_conn(self):
        return self.insta_username, self.insta_password
