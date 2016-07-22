class Contract(object):
    def __init__(self, symbol, sec_type, expiry, right, multiplier, exchange,
                 currency, local_symbol, trading_class, combo_legs, primary_exchange,
                 sec_id_type, sec_id, contract_id=0, strike=0, include_expired=False):
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

        # Pick a non-aggregate (i.e: not the SMART exchange)
        # exchange that the contract trades on.
        # DO NOT SET TO SMART.
        self.primary_exchange = primary_exchange

        # Can not be set to true for orders.
        self.include_expired = include_expired
        self.sec_id_type = sec_id_type
        self.sec_id = sec_id

