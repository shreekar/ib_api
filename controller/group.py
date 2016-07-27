import re


class Group(object):
    def __init__(self, name=None, default_method=None, accounts=None):
        self.name = name
        self.default_method = default_method
        self.accounts = accounts

    def set_all_accounts(self, val):
        self.accounts = [x for x in re.split(' |,', val) if x]
