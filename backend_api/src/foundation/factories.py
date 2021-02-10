from decimal import Decimal
from typing import Union

from src.foundation.money import Money, Currency


def get_money(amount: Union[Decimal, str, float, int]) -> Money:
    return Money(Currency, amount)
