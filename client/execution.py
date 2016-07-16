class Execution(object):
    def __init__(self, order_id, client_id, exec_id, time, acct_number,
                 exchange, side, shares, price, perm_id, liquidation,
                 cum_qty, avg_price, order_ref, ev_rule, ev_multiplier):
        self.order_id = order_id
        self.client_id = client_id
        self.exec_id = exec_id
        self.time = time
        self.acct_number = acct_number
        self.exchange = exchange
        self.side = side
        self.shares = shares
        self.price = price
        self.perm_id = perm_id
        self.liquidation = liquidation
        self.cum_qty = cum_qty
        self.avg_price = avg_price
        self.order_ref = order_ref
        self.ev_rule = ev_rule
        self.ev_multiplier = ev_multiplier
