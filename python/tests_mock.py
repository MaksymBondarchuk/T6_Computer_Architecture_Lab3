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
    def test_create(self):
        self.assertEqual(file_server.error_file_exists,
                         file_server.add('Lab 1', 'About', 'State'))
        self.assertEqual(file_server.result_OK,
                         file_server.add('Lab for test', 'About', 'State'))

    def test_delete(self):
        self.assertEquals(file_server.error_no_file,
                          file_server.delete('Not existed lab'),
                          'Testing for deleting nothing')
        self.assertEquals(file_server.result_OK,
                          file_server.delete('Lab for test'),
                          'Testing for deleting existing lab')


if __name__ == '__main__':
    # mock = Mock(return_value='Heil')
    # mock.return_value = 'Heil'
    # print(mock())
    unittest.main()