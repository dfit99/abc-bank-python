import datetime

from nose.tools import assert_equals, assert_almost_equals

from account import Account, CHECKING, MAXI_SAVINGS, SAVINGS, createBankAccount
from bank import Bank
from customer import Customer

ONE_YEAR_AGO = datetime.datetime.today() - datetime.timedelta(days=365)


def test_customer_summary():
    bank = Bank()
    john = Customer("John").openAccount(createBankAccount(CHECKING))
    bank.addCustomer(john)
    assert_equals(bank.customerSummary(),
                  "Customer Summary\n - John (1 account)")


def test_checking_account():
    bank = Bank()
    checkingAccount = createBankAccount(CHECKING)
    bill = Customer("Bill").openAccount(checkingAccount)
    bank.addCustomer(bill)
    checkingAccount.deposit(100.0, ONE_YEAR_AGO)
    assert_equals(bank.totalInterestPaid(), 0.1)


def test_savings_account(self):
    bank = Bank()
    checkingAccount = createBankAccount(SAVINGS)
    bank.addCustomer(Customer("Bill").openAccount(checkingAccount))
    checkingAccount.deposit(1500.0, ONE_YEAR_AGO)
    assert_equals(bank.totalInterestPaid(), 2.0)


def test_daily_accrued_interest(self):
    bank = Bank()
    checkingAccount = createBankAccount(CHECKING)
    bank.addCustomer(Customer("Bill").openAccount(checkingAccount))

    two_years_ago = datetime.datetime.today() - datetime.timedelta(days=730)
    checkingAccount.deposit(1000.0, transactionDate=two_years_ago)
    assert_equals(checkingAccount.interestEarned(), 2.0)

    checkingAccount.deposit(1000.0, transactionDate=ONE_YEAR_AGO)
    assert_almost_equals(checkingAccount.interestEarned(), 3.0, places=2)

    half_year_ago = datetime.datetime.today() - datetime.timedelta(days=182)
    checkingAccount.deposit(1000.0, transactionDate=half_year_ago)
    assert_almost_equals(checkingAccount.interestEarned(), 3.5, places=2)