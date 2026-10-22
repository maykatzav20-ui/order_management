from enum import Enum


class CustomerType(Enum):
    REGULAR = "REGULAR"
    VIP = "VIP"


class PaymentType(Enum):
    CREDIT_CARD = "CREDIT CARD"
    CASH = "CASH"
    CHECK = "CHECK"
    OTHER = "OTHER"
