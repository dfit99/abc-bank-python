from nose.tools import assert_is_instance, assert_equals

from transaction import Transaction


def test_type():
    t = Transaction(5)
    assert_is_instance(t, Transaction, "correct type")


def test_description():
    t = Transaction(-4)
    assert_equals(t.transactionDescription(), "withdrawal")

    t = Transaction(5)
    assert_equals(t.transactionDescription(), "deposit")