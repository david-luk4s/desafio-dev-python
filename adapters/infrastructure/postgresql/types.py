from domain.entities.transaction import TypeTransaction

class TypeTransactionImpl:
    '''Docstring class'''
    db_postgres : any

    def __init__(self, db_postgres: any) -> None:
        self.db_postgres = db_postgres

    def save(self, type_transaction: TypeTransaction) -> bool:
        '''description docstring'''
        create_type_transaction = """
            INSERT INTO type_transaction(id_type, description, nature, signal) VALUES(%s,%s,%s,%s);
        """
        self.db_postgres.execute(create_type_transaction, (
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
        self.db_postgres.execute(get_type_transactions)
        for row in self.db_postgres.fetchall():
            type_transaction = TypeTransaction(row[0],row[1],row[2],row[3])
            type_transactions[type_transaction.id_type_transaction] = type_transaction

        return type_transactions
