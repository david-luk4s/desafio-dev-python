from dataclasses import dataclass

@dataclass
class Store:
    """ Class for keeping track item of stores."""
    id_store : int
    balance : float
    store_name : str
    store_owner : str

    def __init__(self, store_name: str, store_owner: str, id_store: int = None, balance: float = 0) -> None:
        self.id_store = id_store
        self.balance = balance
        self.store_name = store_name
        self.store_owner = store_owner
