from datetime import date, time

from domain.entitites import recipient
from domain.entitites import card
from domain.entitites import store

class TypeTransaction(object):
    ID : int
    Description: str
    Nature: str
    Signal: str

    def __init__(self,id: int, description: str, nature: str, signal: str) -> None:
        self.ID = id
        self.Description = description
        self.Nature = nature
        self.Signal = signal


class Transaction(object):
    ID : int
    TypeTransaction : TypeTransaction
    DateOccurrence : date
    Value : float
    Recipient : recipient.Recipient
    Card : card.Card
    HourOccurrence : time
    Store : store.Store

    def __init__(self, 
                 id: int, type_transaction: TypeTransaction,
                 date_occurrence: date, value: float,
                 recipient: recipient.Recipient,
                 card: card.Card, hour_occurrence: time,
                 store: store.Store) -> None:
        self.ID = id
        self.TypeTransaction = type_transaction
        self.DateOccurrence = date_occurrence
        self.Value = value
        self.Recipient = recipient
        self.Card = card
        self.HourOccurrence = hour_occurrence
        self.Store = store
