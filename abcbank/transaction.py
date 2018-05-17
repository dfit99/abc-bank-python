from datetime import datetime


class Transaction:
    def __init__(self, amount, transactionDate=None):
        self.amount = amount
        self.transactionDate = transactionDate or datetime.now()

    def transactionDescription(self):
        if self.amount < 0:
            return "withdrawal"
        return "deposit"
