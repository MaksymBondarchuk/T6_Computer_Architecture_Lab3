from mock import *
import unittest

import web_server
import file_server

__author__ = 'Maxim'


class Test(unittest.TestCase):
    @patch('file_server.read')
    def test_read(self, smth):
        mock = Mock(return_value={"name": "Lab1", "about": "About something", "state": "Completed"})
        # a.return_value = {"name": "Lab1", "about": "About something", "state": "Completed"}
        # return_value = a
        res = web_server.bottle_read()
        # a()
        smth.return_value = mock
        assert res

        # a.read.side_effect = []
        # mock_urlopen.return_value = a
        # res = main.download_mp3('https://ia902508.us.archive.org/5/items/testmp3testfile/mpthreetest.mp3', '')
        # assert not res

    # Testing file server
    def test_file_server_create(self):
        self.assertEqual(file_server.result_OK,
                         file_server.add('Lab for test'))
        self.assertEqual(file_server.error_file_exists,
                         file_server.add('Lab for test'))

    def test_file_server_read(self):
        assert file_server.read()

    def test_file_server_update(self):
        file_server.add('Lab for test 2')
        file_server.add('Lab for test')
        self.assertEqual(file_server.error_file_exists,
                         file_server.update('Lab for test', 'name', 'Lab for test 2'))
        file_server.delete('Lab for test 2')
        file_server.delete('Lab for test')

    def test_file_server_delete(self):
        self.assertEquals(file_server.error_no_file,
                          file_server.delete('Not existed lab'))
        self.assertEquals(file_server.result_OK,
                          file_server.delete('Lab for test'))


if __name__ == '__main__':
    unittest.main()