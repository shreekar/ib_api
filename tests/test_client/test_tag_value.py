import unittest

from client.tag_value import TagValue


class TagValueTestCase(unittest.TestCase):
    def test_can_create(self):
        self.assertTrue(TagValue('tag', 'value'))

    def test_compare_tag_value_instances(self):
        instance1 = TagValue('tag1', 'value1')
        self.assertEqual(instance1, instance1)
        instance2 = TagValue('tag1', 'value1')
        instance3 = TagValue('tag2', 'value2')
        instance4 = TagValue('tag1', 'value2')
        self.assertEqual(instance1, instance2)
        self.assertNotEqual(instance1, instance3)
        self.assertNotEqual(instance1, instance4)
