from typing import Dict, List

from src.account.entities import Transaction, Account
from src.account.value_objects import TransactionId
from src.account.use_cases import CreateTransactionInputDto
from src.foundation import get_money


class InMemoryAccountRepository():
    def __init__(self, account: Account):
        self._account = account

    def get(self, transactionId: TransactionId) -> Transaction:
        transaction = None
        try:
            transaction = self._account.transactions[transactionId]
        except IndexError:
            pass

        return transaction 

    def save(self, input_dto: CreateTransactionInputDto) -> Transaction:
        transaction = self._account.transaction(input_dto.type, input_dto.amount) 

        return transaction

    def list_all(self) -> List[Transaction]:
        return [t for t in self._account.transactions.values()] 

    @classmethod
    def build(cls) -> "InMemoryAccountRepository":
        account = Account(get_money(0))

        return cls(account)
         
