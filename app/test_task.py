import unittest
from unittest.mock import patch
import task

mock = {
            'id': 1,
            'description': "Cozinhar",
            'status': 'feito'
        }

class TestTask(unittest.TestCase):
    def tearDown(self):
        task.tasks = []
    
    @patch('builtins.print', return_value='')
    def test_should_add_task_to_list(self, mock_print):
        task.add_task(mock)
        self.assertIn(mock, task.tasks)
    
    @patch('builtins.print', return_value='')
    @patch('builtins.input', return_value='1')
    def test_should_remove_task_from_list(self, mock_input, mock_print):
        task.add_task(mock)
        task.remove_task()
        self.assertNotIn(mock, task.tasks)
    
    
    @patch('builtins.print', return_value='')
    @patch('builtins.input', side_effect=['1', 'arquivado'])
    def test_should_alter_task(self, mock_print, mock_input):
        task.add_task(mock)
        task.alter_task()
        self.assertEqual('arquivado', task.tasks[0]["status"])
    
    
    @patch('builtins.print', return_value='')
    @patch('builtins.input', side_effect=['2'])
    def test_should_not_found_when_alter_task(self, mock_input, mock_print):
        task.add_task(mock)
        task.alter_task()
        mock_print.assert_called_with("Task not found.")

    
    @patch('builtins.print')
    def test_should_show_all_tasks(self, mock_print):
        task.add_task(mock)
        task.list_tasks()
        expected_calls = [
            unittest.mock.call("Tasks:"),
            unittest.mock.call("1. ID: 1, Description: Cozinhar, Status: arquivado")
        ]

        mock_print.assert_has_calls(expected_calls, any_order=False)
    
    
    @patch('builtins.print')
    def test_should_show_no_tasks(self, mock_print):
        task.list_tasks()
        
        mock_print.assert_called_once_with("No tasks found.")
    
    
    @patch('builtins.input', side_effect=['Estudar', 'não feito'])
    def test_should_create_task(self, mock_input):
        new_task = task.create_task()
        
        self.assertEqual({'id': 1, 'description': 'Estudar', 'status': 'não feito' }, new_task)
    
if __name__ == '__main__':
    unittest.main()