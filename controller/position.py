class Position(object):
    def __init__(self, contract, account, position,
                 market_price, market_value, average_cost,
                 unreal_pnl, real_pnl):
        self.contract = contract
        self.account = account
        self.position = position
        self.market_price = market_price
        self.market_value = market_value
        self.average_cost = average_cost
        self.unreal_pnl = unreal_pnl
        self.real_pnl = real_pnl
