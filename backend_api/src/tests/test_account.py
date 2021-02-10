import pytest
from decimal import Decimal

from src.account import Account, TypeTransaction
from src.account.exceptions import InsufficientBalanceException
from src.foundation import Money, Currency


def test_create_account():
    money = Money(Currency, 0)

    account = Account(money)

    assert account.balance == money

def test_create_account_with_balance():
    money = Money(Currency, 1.1)

    account = Account(money)

    assert account.balance == Money(Currency, 1.1)

def test_credit_transaction():
    money = Money(Currency, 0)
    account = Account(money)
    amount = Money(Currency, 100)

     
    account.transaction(TypeTransaction.CREDIT, amount)

    assert account.balance == amount

def test_debit_transaction():
    money = Money(Currency, 400)
    account = Account(money)
    amount = Money(Currency, 245.25)
    expected = Money(Currency, 154.75)

    account.transaction(TypeTransaction.DEBIT, amount)

    assert account.balance == expected

def test_cannot_spend_more_than_balance():
    money = Money(Currency, 0)
    account = Account(money)
    amount = Money(Currency, 25)
    expected = Money(Currency, 0)

    with pytest.raises(InsufficientBalanceException):
        account.transaction(TypeTransaction.DEBIT, amount)
