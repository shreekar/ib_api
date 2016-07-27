import unittest

from controller.instrument import Instrument


class InstrumentTestCase(unittest.TestCase):
    def test_can_create(self):
        self.assertTrue(Instrument)

    def test_str_representation(self):
        self.assertEqual('FUT.US', str(Instrument.FUT_US))
        self.assertEqual('BOND', str(Instrument.BOND))
