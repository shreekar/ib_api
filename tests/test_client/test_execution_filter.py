import unittest

from client.execution_filter import ExecutionFilter


class ExecutionFilterTestCase(unittest.TestCase):
    def test_can_create(self):
        instance = ExecutionFilter(client_id=1, acct_code=420, time='test',
                                   symbol='GOOG', sec_type='Technology',
                                   exchange='NYSE', side='right?')
        self.assertTrue(instance)

    def test_compare_execution_filters(self):
        instance1 = ExecutionFilter(client_id=1, acct_code=420, time='test',
                                    symbol='GOOG', sec_type='Technology',
                                    exchange='NYSE', side='right?')
        instance2 = ExecutionFilter(client_id=2, acct_code=420, time='test',
                                    symbol='GOOG', sec_type='Technology',
                                    exchange='NYSE', side='right?')
        instance3 = ExecutionFilter(client_id=1, acct_code=420, time='test',
                                    symbol='GOOGL', sec_type='Technology',
                                    exchange='NYSE', side='right?')
        instance4 = ExecutionFilter(client_id=1, acct_code=420, time='test',
                                    symbol='GOOG', sec_type='Technology',
                                    exchange='NYSE', side='right')
        instance5 = ExecutionFilter(client_id=1, acct_code=420, time='test',
                                    symbol='GOOG', sec_type='Technology',
                                    exchange='NYSE', side='right?')
        self.assertEqual(instance1, instance1)
        self.assertEqual(instance1, instance5)
        self.assertNotEqual(instance1, instance2)
        self.assertNotEqual(instance1, instance3)
        self.assertNotEqual(instance1, instance4)
        self.assertNotEqual(instance2, instance5)
