class Contract(object):
    def __init__(self, contract_id, symbol, sec_type, expiry, strike,
                 right, multiplier, exchange, currency, local_symbol,
                 trading_class, combo_legs, primary_exchange, include_expired,
                 sec_id_type, sec_id):
        self.contract_id = contract_id
        self.symbol = symbol
        self.sec_type = sec_type
        self.expiry = expiry
        self.strike = strike
        self.right = right
        self.multiplier = multiplier
        self.exchange = exchange
        self.currency = currency
        self.local_symbol = local_symbol
        self.trading_class = trading_class
        self.combo_legs = combo_legs
        self.primary_exchange = primary_exchange
        self.include_expired = include_expired
        self.sec_id_type = sec_id_type
        self.sec_id = sec_id

