class OptContract(object):
    def __init__(self, symbol, expiry, strike, right, exchange='SMART'):
        self.symbol = symbol
        self.expiry = expiry
        self.strike = strike
        self.right = right
        self.exchange = exchange
        self.sec_type = 'OPT'
        self.currency = 'USD'
