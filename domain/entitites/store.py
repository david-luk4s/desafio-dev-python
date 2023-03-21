class Store(object):
    ID : int
    Balance : float
    StoreName : str
    StoreOwner : str

    def __init__(self, id: int, store_name: str, store_owner: str) -> None:
        self.ID = id
        self.Balance = 0
        self.StoreName = store_name
        self.StoreOwner = store_owner
