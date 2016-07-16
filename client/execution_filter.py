class ExecutionFilter(object):
    def __init__(self, client_id, acct_code, time, symbol, sec_type, exchange, side):
        self.client_id = client_id
        self.acct_code = acct_code
        self.time = time
        self.symbol = symbol
        self.sec_type = sec_type
        self.exchange = exchange
        self.side = side

    def __eq__(self, other):
        return self.client_id == other.client_id and \
               self.acct_code == other.acct_code and \
               self.time == other.time and \
               self.symbol == other.symbol and \
               self.sec_type == other.sec_type and \
               self.exchange == other.exchange and \
               self.side == other.side
