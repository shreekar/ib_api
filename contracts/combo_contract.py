class ComboContract(object):
    def __init__(self, symbol, currency='USD', exchange='SMART'):
        self.symbol = symbol
        self.currency = currency
        self.exchange = exchange
        self.sec_type = 'BAG'