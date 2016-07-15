import unittest

from client.any_wrapper import AnyWrapper


class AnyWrapperTestCase(unittest.TestCase):
    def test_error(self):
        msg = "Error msg appears here"
        self.assertEqual(msg, AnyWrapper.error(msg))

    def test_build_error(self):
        expected = '1 | 404 | Can not find resource'
        self.assertEqual(expected, AnyWrapper.build_error(1, 404, 'Can not find resource'))

    def test_connection_closed(self):
        self.assertEqual('Connection Closed', AnyWrapper.connection_closed())
