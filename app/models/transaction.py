class Transaction:
    def __init__(self, amount, merchant, tag, ts=None, id = None):
        self.amount = amount
        self.merchant = merchant
        self.tag = tag
        self.id = id
