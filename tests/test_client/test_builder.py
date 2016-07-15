import unittest

from client.builder import Builder


class BuilderTestCase(unittest.TestCase):
    def test_can_create(self):
        self.assertTrue(Builder())
