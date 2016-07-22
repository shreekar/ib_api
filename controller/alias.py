class Alias(object):
    def __init__(self, account, alias):
        self.account = account
        self.alias = alias

    def __str__(self):
        return self.account + '/' + self.alias
