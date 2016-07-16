class FutContract(object):
    def __init__(self, symbol, expiry, currency='USD'):
        self.symbol = symbol
        self.expiry = expiry
        self.currency = currency
        self.sec_type = 'FUT'
        self.exchange = 'ONE'
