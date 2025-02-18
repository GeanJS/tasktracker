import unittest
from unittest.mock import patch, mock_open, call
import task
import json

mock = {
            'id': 1,
            'description': "Cozinhar",
            'status': 'feito'
        }

mock_list = [mock]

class TestTask(unittest.TestCase):
    def tearDown(self):
        task.tasks = []
        mock_list.clear()
        mock_list.append(mock)
    
    @patch('builtins.print', return_value='')
    @patch('task.save_tasks')
    @patch('task.load_tasks', return_value=[])
    def test_should_add_task_to_list(self, mock_load_tasks, mock_save_tasks, mock_print):
        task.add_task(task.tasks, mock)
        self.assertIn(mock, task.tasks)
        mock_save_tasks.assert_called_once_with(task.tasks)
        mock_print.assert_called_once_with("Task added.")
    
    
    @patch('builtins.print')
    @patch('builtins.input', return_value='1')
    @patch('task.save_tasks')
    @patch('task.load_tasks', return_value=mock_list)
    def test_should_remove_task_from_list(self, mock_load_tasks, mock_save_tasks, mock_input, mock_print):
        task.remove_task(mock_list)
        self.assertNotIn(mock, mock_list)
        mock_save_tasks.assert_called_once_with(mock_list)
        mock_print.assert_called_once_with(f"Task removed: {mock}")
    
    
    @patch('builtins.print', return_value='')
    @patch('builtins.input', side_effect=['1', 'arquivado'])
    @patch('task.save_tasks')
    @patch('task.load_tasks', return_value=mock_list)
    def test_should_alter_task(self, mock_load_tasks, mock_save_tasks, mock_input, mock_print):
        task.alter_task(mock_list)
        self.assertEqual('arquivado', mock_list[0]["status"])
        mock_save_tasks.assert_called_once_with(mock_list)
        mock_print.assert_called_once_with(f"Task ID 1 updated. New status: arquivado")
    
    
    @patch('builtins.print', return_value='')
    @patch('builtins.input', side_effect=['2'])
    @patch('task.load_tasks', return_value=mock_list)
    def test_should_not_found_when_alter_task(self, mock_load_tasks, mock_input, mock_print):
        task.alter_task(mock_list)
        mock_print.assert_called_with("Task not found.")

    
    @patch('builtins.print')
    @patch('task.load_tasks', return_value=mock_list)
    def test_should_show_all_tasks(self, mock_load_tasks, mock_print):
        task.list_tasks(mock_list)
        expected_calls = [
            call(json.dumps(mock_list, indent=2))
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)
    
    
    @patch('builtins.print')
    @patch('task.load_tasks', return_value=[])
    def test_should_show_no_tasks(self, mock_load_tasks, mock_print):
        task.list_tasks([])
        mock_print.assert_called_once_with("Task list empty\n")
    
    
    @patch('builtins.input', side_effect=['Estudar', 'não feito'])
    @patch('task.load_tasks', return_value=[])
    def test_should_create_task(self, mock_load_tasks, mock_input):
        new_task = task.create_task([])
        self.assertEqual({'id': 1, 'description': 'Estudar', 'status': 'não feito' }, new_task)
    
if __name__ == '__main__':
    unittest.main()