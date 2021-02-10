from typing import Dict
import uuid
from datetime import datetime

from src.account.value_objects import TransactionId, TypeTransaction
from src.account.exceptions import InsufficientBalanceException
from src.foundation import Money, ReadersWriteLock

class Account:
    def __init__(self, value: Money):
        self._balance = value
        self._transactions: Dict[TransactionId, Transaction] = {}
        self.rw = ReadersWriteLock()

    def transaction(self, type:TypeTransaction, amount: Money) -> "Transaction":
        transaction = Transaction.create(type, amount)

        if (type == TypeTransaction.DEBIT): 
            self.debitTransaction(amount, transaction)
        elif (type == TypeTransaction.CREDIT):
            self.creditTransanction(amount, transaction)
        else:
            raise Exception("InvalidTypeTransaction")

        return transaction

    def debitTransaction(self, amount, transaction):
        self.rw.acquire_write_lock()
        try:
            if self._balance < amount:
                raise InsufficientBalanceException()

            self._balance -= amount
            self._transactions[transaction.id] = transaction    
        finally:
            self.rw.release_write_lock()

    def creditTransanction(self, amount, transaction):
        self.rw.acquire_write_lock()
        try:
            self._balance += amount
            self._transactions[transaction.id] = transaction    
        finally:
            self.rw.release_write_lock()

    @property
    def balance(self):
        try:
            self.rw.acquire_read_lock()
            return self._balance
        finally:
            self.rw.release_read_lock()
        
    @property
    def transactions(self):
        try:
            self.rw.acquire_read_lock()
            return self._transactions
        finally:
            self.rw.release_read_lock()

class Transaction:
    def __init__(self, id: TransactionId, type: TypeTransaction, amount: Money, date: datetime):
        self.id= id
        self.type= type
        self.amount= amount
        self.effectiveDate= date

    @classmethod
    def create(cls, type:TypeTransaction, amount: Money) -> "Transaction":
        id = uuid.uuid4()
        date = datetime.now()

        return cls(str(id), type, amount, date)
