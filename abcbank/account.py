from datetime import datetime

from abcbank.transaction import Transaction


CHECKING = 0
SAVINGS = 1
MAXI_SAVINGS = 2
DAYS_IN_YEAR = 365


class Account:
    def __init__(self):
        self.transactions = []

    def deposit(self, amount, transactionDate=None):
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        else:
            self.transactions.append(Transaction(amount, transactionDate))

    def withdraw(self, amount, transactionDate=None):
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        else:
            self.transactions.append(Transaction(-amount, transactionDate))

    def _calculateInterest(self, checkAllTransactionsUpInToIndex=None, daysAccrued=365):
        fractionOfYearAccrued = daysAccrued/DAYS_IN_YEAR
        amount = self.sumTransactions(checkAllTransactionsUpInToIndex)
        interestAmount =  0.01


        if self.accountType == SAVINGS:
            if (amount <= 1000):
                interestAmount = 0.001
                return amount * interestAmount * fractionOfYearAccrued
            else:
                interestAmount = 0.002
                return 1 + (amount - 1000) * interestAmount * fractionOfYearAccrued
        elif self.accountType == MAXI_SAVINGS:
            if (amount <= 1000):
                currTime = datetime.now()
                interestAmount = 0.02
                if abs(self.transactions[-1].transactionDate - currTime <= datetime.timedelta(days=10)):
                    interestAmount = 0.01
                return amount * interestAmount * fractionOfYearAccrued
            elif (amount <= 2000):
                interestAmount = 0.05
                return 20 + (amount - 1000) * interestAmount * fractionOfYearAccrued
            else:
                interestAmount = 0.1
                return 70 + (amount - 2000) * interestAmount * fractionOfYearAccrued
        else:
            return amount * interestAmount * fractionOfYearAccrued

    def sumTransactions(self, checkAllTransactionsUpToIndex=None):
        endIndex = checkAllTransactionsUpToIndex or len(self.transactions)
        return sum([t.amount for t in self.transactions[0:endIndex]])

    def interestEarned(self):
        """Calculate Accrued Interest (daily)"""

        transactions = self.transactions
        totalInterest = 0

        for ind in range(1, len(transactions)):
            prevTransaction = transactions[ind-1]
            currTransaction = transactions[ind]
            timeLagDays = (currTransaction.transactionDate - prevTransaction.transactionDate).days
            totalInterest += self._calculateInterest(checkAllTransactionsUpInToIndex=ind, daysAccrued=timeLagDays)
        totalInterest += self._calculateInterest(
            daysAccrued=(datetime.now() - self.transactions[-1].transactionDate).days)
        return totalInterest

    @property
    def accountDescription(self):
        return 'Account'

class CheckingAccount(Account):
    accountType = CHECKING

    def _calculateInterest(self, checkAllTransactionsUpInToIndex=None, daysAccrued=365):
        fractionOfYearAccrued = daysAccrued / DAYS_IN_YEAR
        amount = self.sumTransactions(checkAllTransactionsUpInToIndex)
        return amount * 0.001 * fractionOfYearAccrued

    @property
    def accountDescription(self):
        return "Checking Account"
class SavingsAccount(Account):
    accountType = SAVINGS

    def _calculateInterest(self, checkAllTransactionsUpInToIndex=None, daysAccrued=365):
        fractionOfYearAccrued = daysAccrued / DAYS_IN_YEAR
        amount = self.sumTransactions(checkAllTransactionsUpInToIndex)

        if (amount <= 1000):
            interestAmount = 0.001
            return amount * interestAmount * fractionOfYearAccrued
        else:
            interestAmount = 0.002
            return 1 + (amount - 1000) * interestAmount * fractionOfYearAccrued

    @property
    def accountDescription(self):
        return "Savings Account"


class MaxiSavings(Account):
    accountType = MAXI_SAVINGS

    def _calculateInterest(self, checkAllTransactionsUpInToIndex=None, daysAccrued=365):
        fractionOfYearAccrued = daysAccrued / DAYS_IN_YEAR
        amount = self.sumTransactions(checkAllTransactionsUpInToIndex)

        if (amount <= 1000):
            currTime = datetime.now()
            interestAmount = 0.02
            if abs(self.transactions[-1].transactionDate - currTime <= datetime.timedelta(days=10)):
                interestAmount = 0.01
            return amount * interestAmount * fractionOfYearAccrued
        elif (amount <= 2000):
            interestAmount = 0.05
            return 20 + (amount - 1000) * interestAmount * fractionOfYearAccrued
        else:
            interestAmount = 0.1
            return 70 + (amount - 2000) * interestAmount * fractionOfYearAccrued

    @property
    def accountDescription(self):
        return "Maxi Savings Account"


def createBankAccount(accountType):
    if  accountType == CHECKING:
        return CheckingAccount()
    elif accountType == SAVINGS:
        return SavingsAccount()
    elif accountType == MAXI_SAVINGS:
        return MaxiSavings()
    raise ValueError("Account Type: {AccountType} is not supported".format(accountType))
