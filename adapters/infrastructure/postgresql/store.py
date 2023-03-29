from domain.entities.store import Store
from domain.entities.transaction import Transaction

class StoreImpl:
    '''Docstring class'''
    cursor : any

    def __init__(self, cursor: any) -> None:
        self.cursor = cursor

    def get_or_create(self, store: Store) -> bool:
        '''description docstring'''
        get_store = """
            SELECT id, balance, store_name, store_owner FROM store WHERE store_name=%s;
        """
        create_store = """
            INSERT INTO store(store_name, store_owner) VALUES(%s,%s) RETURNING id;
        """
        self.cursor.execute(get_store, (store.store_name,))
        rst = self.cursor.fetchone()

        if rst:
            store.id_store = rst[0]
            store.balance = float(str(rst[1]))
        else:
            self.cursor.execute(create_store, (store.store_name,store.store_owner))
            rst = self.cursor.fetchone()
            store.id_store = rst[0]

        return True

    def update_balance(self, transaction: Transaction) -> None:
        '''Update balance of store'''
        balance : float
        update_store = """
            UPDATE store SET balance=%s WHERE id=%s;
        """

        if transaction.type_transaction.signal == "+":
            balance = transaction.store.balance + transaction.value
        else:
            balance = transaction.store.balance - transaction.value

        self.cursor.execute(update_store, (balance, transaction.store.id_store))
