from datetime import date, time
from dataclasses import dataclass

from domain.entities import recipient as outside_rc
from domain.entities import card as outside_cd
from domain.entities import store as outside_st

@dataclass
class TypeTransaction:
    """Class for keeping track item of type transactions."""
    id_type_transaction : int
    description: str
    nature: str
    signal: str

    def __init__(self,
                 id_type_transaction: int,
                 description: str,
                 nature: str,
                 signal: str) -> None:
        self.id_type_transaction = id_type_transaction
        self.description = description
        self.nature = nature
        self.signal = signal


@dataclass
class Transaction:
    """Class for keeping track item of transactions."""
    id_transaction : int
    type_transaction : TypeTransaction
    date_occurrence : date
    value : float
    recipient : outside_rc.Recipient
    card : outside_cd.Card
    hour_occurrence : time
    store : outside_st.Store

    def __init__(self,
                 type_transaction: TypeTransaction,
                 date_occurrence: date, value: float,
                 recipient: outside_rc.Recipient,
                 card: outside_cd.Card, hour_occurrence: time,
                 store: outside_st.Store, id_transaction: int = None) -> None:
        self.id_transaction = id_transaction
        self.type_transaction = type_transaction
        self.date_occurrence = date_occurrence
        self.value = value
        self.recipient = recipient
        self.card = card
        self.hour_occurrence = hour_occurrence
        self.store = store
