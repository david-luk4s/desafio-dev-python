from domain.entities.transaction import TypeTransaction

class TypeTransactionImpl:
    '''Docstring class'''
    cursor : any

    def __init__(self, cursor: any) -> None:
        self.cursor = cursor

    def save(self, type_transaction: TypeTransaction) -> bool:
        '''description docstring'''
        create_type_transaction = """
            INSERT INTO type_transaction(id_type, description, nature, signal) VALUES(%s,%s,%s,%s);
        """
        self.cursor.execute(create_type_transaction, (
            type_transaction.id_type_transaction,
            type_transaction.description,
            type_transaction.nature,
            type_transaction.signal
        ))
        return True

    def get_all(self) -> dict[TypeTransaction]:
        '''Get all type transactions'''
        type_transactions: dict[TypeTransaction] = dict()
        get_type_transactions = """
            SELECT id_type, description, nature, signal FROM type_transaction
        """
        self.cursor.execute(get_type_transactions)
        for row in self.cursor.fetchall():
            type_transaction = TypeTransaction(row[0],row[1],row[2],row[3])
            type_transactions[type_transaction.id_type_transaction] = type_transaction

        return type_transactions
