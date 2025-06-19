
import unittest
from unittest.mock import mock_open, patch
import builtins


from part_1 import load_params, write_log, PARAMS

class TestLoadParams(unittest.TestCase):
    def setUp(self):
        self.orig = PARAMS.copy()

    def tearDown(self):
        PARAMS.clear()
        PARAMS.update(self.orig)

    def test_file_not_found(self):
        with patch.object(builtins, 'open', side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                load_params('no_such.ini')

    def test_permission_error(self):
        with patch.object(builtins, 'open', side_effect=PermissionError):
            with self.assertRaises(PermissionError):
                load_params('protected.ini')

    def test_invalid_format_no_equals(self):
        data = "precision 0.1\n"
        m = mock_open(read_data=data)
        with patch.object(builtins, 'open', m):
            with self.assertRaises(ValueError) as cm:
                load_params('params.ini')
            self.assertIn("нет символа '='", str(cm.exception))

    def test_empty_key(self):
        data = "=123\n"
        m = mock_open(read_data=data)
        with patch.object(builtins, 'open', m):
            with self.assertRaises(ValueError) as cm:
                load_params('params.ini')
            self.assertIn("пустой ключ", str(cm.exception))

    def test_invalid_eval(self):
        data = "precision = not_a_number\n"
        m = mock_open(read_data=data)
        with patch.object(builtins, 'open', m):
            with self.assertRaises(Exception):
                load_params('params.ini')

    def test_successful_load(self):
        data = "precision = 0.02\ndest = out.txt\n"
        m = mock_open(read_data=data)
        with patch.object(builtins, 'open', m):
            params = load_params('params.ini')
        self.assertEqual(params['precision'], 0.02)
        self.assertEqual(params['dest'], 'out.txt')


class TestWriteLog(unittest.TestCase):
    def test_write_success(self):
        m = mock_open()
        with patch.object(builtins, 'open', m):
            write_log(1, 2, action='sum', result=3, file='log.txt')
        m.assert_called_with('log.txt', mode='a', errors='ignore')

    def test_main_permission_then_backup(self):
        m = mock_open()
        m.side_effect = [PermissionError, m.return_value]
        with patch.object(builtins, 'open', m):
            write_log(1, 2, action='sum', result=3, file='log.txt')
        calls = [call_args[0][0] for call_args in m.call_args_list]
        self.assertEqual(calls, ['log.txt', 'log.txt.txt'])

    def test_both_permission_error(self):
        def raiser(*args, **kwargs):
            raise PermissionError
        with patch.object(builtins, 'open', side_effect=raiser):
            with self.assertRaises(PermissionError):
                write_log(1, 2, action='sum', result=3, file='log.txt')


if __name__ == '__main__':
    unittest.main()
