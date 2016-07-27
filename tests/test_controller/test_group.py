import unittest

from controller.group import Group


class GroupTestCase(unittest.TestCase):
    def setUp(self):
        self.group = Group()
        self.expacted = ['IB', 'API', 'in', 'Python']

    def _set_group_accounts(self, val):
        self.group.set_all_accounts(val)
        return self.group.accounts

    def test_set_all_accounts(self):
        self.assertEqual(self.expacted, self._set_group_accounts('IB , API in Python,'))
        self.assertEqual(self.expacted, self._set_group_accounts('IB API in Python'))
        self.assertEqual(self.expacted, self._set_group_accounts('IB, API, in, Python'))
