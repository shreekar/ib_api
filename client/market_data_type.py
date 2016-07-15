class MarketDataType(object):
    REALTIME = 1
    FROZEN = 2

    @classmethod
    def get_field(cls, market_data_type):
        if market_data_type == cls.REALTIME:
            return 'Real-Time'
        elif market_data_type == cls.FROZEN:
            return 'Frozen'
        else:
            return 'Unknown'
