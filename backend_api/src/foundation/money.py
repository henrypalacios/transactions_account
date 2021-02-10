from typing import Type, Any
import inspect
from decimal import Decimal, DecimalException


class Currency:
    decimal_precision=2
    code="$"
    def __str__(self) ->str:
        return "%s" % self.code

class Money:
    def __init__(self, currency: Type[Currency], amount: Any) -> None:
        if not inspect.isclass(currency) and not issubclass(currency, Currency):
            raise ValueError('%s is not a subclass of Currency.' % currency)
        
        try:
            decimal_amount = Decimal(amount).normalize()
        except DecimalException: 
            raise ValueError('%s is not a valid amount.' % amount)

        
        self._currency = currency
        self._amount = decimal_amount

    @property
    def currency(self) -> Type[Currency]:
        return self._currency

    @property
    def amount(self) -> Decimal:
        return self._amount

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            raise TypeError
        return self.currency == other.currency and self.amount == other.amount

    def __add__(self, other: "Money") -> "Money":
        if not isinstance(other, Money) or not self.currency == other.currency:
            raise TypeError
        return Money(self.currency, self.amount + other.amount)

    def __sub__(self, other: "Money") -> "Money":
        if not isinstance(other, Money) or not self.currency == other.currency:
            raise TypeError
        return Money(self.currency, self.amount - other.amount)

    def __lt__(self, other: "Money") -> bool:
        if not isinstance(other, Money):
            raise TypeError(f"'<' not supported between instances of 'Money' and '{other.__class__.__name__}'")
        else:
            return self.amount < other.amount

    def __str__(self) -> str:
        return f"{self._amount:.{self.currency.decimal_precision}f}{self._currency.code}"
    
    def __repr__(self) -> str:
        return f"Money({self._currency.__name__}, {repr(self._amount)})"
