import unittest

from client.wrapper import Wrapper


class WrapperTestCase(unittest.TestCase):
    def test_error(self):
        msg = "Error msg appears here"
        self.assertEqual(msg, Wrapper.error(msg))

    def test_build_error(self):
        expected = '1 | 404 | Can not find resource'
        self.assertEqual(expected, Wrapper.build_error(1, 404, 'Can not find resource'))

    def test_connection_closed(self):
        self.assertEqual('Connection Closed', Wrapper.connection_closed())
