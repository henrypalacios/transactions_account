from enum import Enum
import uuid


class TypeTransaction(Enum):
    DEBIT="debit"
    CREDIT="credit"

TransactionId = str # str(uuid.UUID)
