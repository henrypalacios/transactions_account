from dataclasses import dataclass
from datetime import datetime
from src.account.entities import Transaction

from src.account.value_objects import TransactionId, TypeTransaction
from src.foundation import Money

@dataclass
class CreateTransactionInputDto:
    type: TypeTransaction
    amount: Money

@dataclass
class TransactionOutputDto:
    id: TransactionId
    type: TypeTransaction
    amount: Money
    effectiveDate: datetime




        
