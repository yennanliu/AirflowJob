from airflow.operators.bash_operator import BashOperator
from airflow.models import BaseOperator
from airflow.contrib.hooks.spark_submit_hook import SparkSubmitHook
import os

class SPARKOperator(BaseOperator):

    def __init__(self, command, dag_folder, env_vars='', *args, **kwargs):
        super(SPARKOperator, self).__init__(*args, **kwargs)
        self.command = command
        self.dag_folder = dag_folder

    def execute(self, context):
        spark_conn = SparkSubmitHook()

        BashOperator(
            task_id=context.get('task').task_id,
            bash_command=self._bash_operator_command()
        ).execute(context)

    def _bash_operator_command(self):
        if get_env() == 'prod':
            profile_dir = '/usr/local/airflow/dags/{dag_folder}'.format(dag_folder=self.dag_folder)
        else:
            profile_dir = '/usr/local/airflow/dags/{dag_folder}'.format(dag_folder=self.dag_folder)

        command = """cd /usr/local/airflow/dags/{dag_folder} && {command} 
        """.format(
            command=self.command,
            dag_folder=self.dag_folder
        )

        return command