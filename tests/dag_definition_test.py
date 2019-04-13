import unittest
from airflow.models import DagBag

class TestHelloWorldDAG(unittest.TestCase):
    """Check HelloWorldDAG expectation"""

    def setUp(self):
        self.dagbag = DagBag()

    def test_task_count(self):
        """Check task count of hello_world dag"""
        dag_id='hello_world'
        dag = self.dagbag.get_dag(dag_id)
        # check if there are 3 tasks in the hello_world DAG 
        self.assertEqual(len(dag.tasks), 3)

    def test_contain_tasks(self):
        """Check task contains in hello_world dag"""
        dag_id='hello_world_dag'
        dag = self.dagbag.get_dag(dag_id)
        tasks = dag.tasks
        task_ids = list(map(lambda task: task.task_id, tasks))
        self.assertListEqual(task_ids, ['START_dag', 'END_dag','hello_task'])

    def test_dependencies_of_dummy_task(self):
        """Check the task dependencies of dummy_task in hello_world dag"""
        dag_id='hello_world_dag'
        dag = self.dagbag.get_dag(dag_id)
        dummy_task = dag.get_task('dummy_task')

        upstream_task_ids = list(map(lambda task: task.task_id, dummy_task.upstream_list))
        self.assertListEqual(upstream_task_ids, ['START_dag'])
        downstream_task_ids = list(map(lambda task: task.task_id, dummy_task.downstream_list))
        self.assertListEqual(downstream_task_ids, ['hello_task', 'END_dag'])

    def test_dependencies_of_hello_task(self):
        """Check the task dependencies of hello_task in hello_world dag"""
        dag_id='hello_world_dag'
        dag = self.dagbag.get_dag(dag_id)
        hello_task = dag.get_task('hello_task')

        upstream_task_ids = list(map(lambda task: task.task_id, hello_task.upstream_list))
        self.assertListEqual(upstream_task_ids, ['START_dag'])
        downstream_task_ids = list(map(lambda task: task.task_id, hello_task.downstream_list))
        self.assertListEqual(downstream_task_ids, ['END_dag'])

suite = unittest.TestLoader().loadTestsFromTestCase(TestHelloWorldDAG)
unittest.TextTestRunner(verbosity=2).run(suite)