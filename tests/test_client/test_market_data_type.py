import unittest

from client.market_data_type import MarketDataType


class MarketDataTypeTestCase(unittest.TestCase):
    def test_can_create(self):
        self.assertTrue(MarketDataType())

    def test_get_field(self):
        self.assertEqual('Real-Time', MarketDataType.get_field(1))
        self.assertEqual('Frozen', MarketDataType.get_field(2))
        self.assertEqual('Unknown', MarketDataType.get_field(5))
        self.assertEqual('Unknown', MarketDataType.get_field(-9))
