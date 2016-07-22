import unittest

from controller.alias import Alias


class AliasTestCase(unittest.TestCase):
    def setUp(self):
        self.alias = Alias('129386', 'AccountAlias')

    def test_can_create(self):
        self.assertTrue(self.alias)

    def test_string_rep(self):
        self.assertEqual('129386/AccountAlias', str(self.alias))
