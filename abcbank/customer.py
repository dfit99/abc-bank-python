from account import CHECKING, SAVINGS, MAXI_SAVINGS


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def openAccount(self, account):
        self.accounts.append(account)
        return self

    def numAccs(self):
        return len(self.accounts)

    def totalInterestEarned(self):
        return sum([a.interestEarned() for a in self.accounts])

    def getStatement(self):
        """This method returns a statement"""
        totalAcrossAllAccounts = sum([a.sumTransactions() for a in self.accounts])
        statements = ''.join([self.statementForAccount(account) for account in self.accounts])
        totalValue = _toDollars(totalAcrossAllAccounts)

        return "Statement for {name}{statements}\n\nTotal In All Accounts {totalValue}".format(name=self.name,
                                                                                               statements=statements,
                                                                                               totalValue=_toDollars(totalAcrossAllAccounts))

    def statementForAccount(self, account):
        accountType = "\n\n{accountDescription}\n".format(accountDescription=account.accountDescription)
        transactionSummary = [t.transactionDescription() + " " + _toDollars(abs(t.amount))
                              for t in account.transactions]
        transactionSummary = "  " + "\n  ".join(transactionSummary) + "\n"
        totalSummary = "Total " + _toDollars(sum([t.amount for t in account.transactions]))

        return "{accountType}{transactionSummary}{totalSummary}".format(accountType=accountType,
                                                                        transactionSummary=transactionSummary,
                                                                        totalSummary=totalSummary)


def _toDollars(number):
    return "${:1.2f}".format(number)
