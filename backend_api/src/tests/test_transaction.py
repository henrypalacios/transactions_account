import pytest
from decimal import Decimal

from src.account import Account, Transaction, TypeTransaction
from src.account.exceptions import InsufficientBalanceException
from src.foundation import Money, Currency


def test_create_transaction():
    money_expected = Money(Currency, 10)
    transaction = Transaction.create(TypeTransaction.CREDIT, Money(Currency, 10))

    assert isinstance(transaction, Transaction)
    assert transaction.amount == money_expected
