import unittest
from client.under_comp import UnderComp


class UnderCompTestCase(unittest.TestCase):
    def test_can_create(self):
        self.assertTrue(UnderComp())

    def test_compare_under_comp_instances(self):
        instance1 = UnderComp(con_id=1, delta=2, price=3)
        self.assertEqual(instance1, instance1)
        self.assertEqual(instance1, UnderComp(con_id=1, delta=2, price=3))
        self.assertNotEqual(instance1, UnderComp(con_id=0, delta=2, price=3))
        self.assertNotEqual(instance1, UnderComp(con_id=1, delta=2, price=4))
