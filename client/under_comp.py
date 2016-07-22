class UnderComp(object):
    def __init__(self, con_id=0, delta=0, price=0):
        self.con_id = con_id
        self.delta = delta
        self.price = price

    def __eq__(self, other):
        return self.con_id == other.con_id and \
            self.delta == other.delta and \
            self.price == other.price
