from datetime import datetime

from domain.entities.store import Store
from domain.entities.recipient import Recipient
from domain.entities.card import Card
from domain.entities.transaction import TypeTransaction, Transaction


class TransactionImpl:
    '''This class is implementation of transaction interface.'''
    db_postgres : any

    def __init__(self, db_postgres: any) -> None:
        self.db_postgres = db_postgres

    def parse(self, tp_transaction: dict[TypeTransaction], block: str) -> list[Transaction]:
        '''Implementation of transaction interface.'''

        items = []
        for row in block.splitlines():
            if row == "":
                continue

            #Type Transaction
            typetransaction_id = int(row[0])

            #Date ocurrence
            date_ocurrence = row[1:9]
            date_ocurrence = datetime.strptime(date_ocurrence, "%Y%m%d")

            #Value
            value = float(row[9:19])
            value = value / 100.00

            #CPF
            cpf = row[19:30]

            #Number card
            card_number = row[30:42]

            #Hour of ocurrence
            hour_ocurrence = row[42:48]
            hour_ocurrence = datetime.strptime(hour_ocurrence, "%H%M%S").time()

            #Data store
            store_owner = row[48:62]
            store_name = row[62:81]

            items.append(
                Transaction(
                    type_transaction=tp_transaction[typetransaction_id],
                    date_occurrence=date_ocurrence,
                    value=value,
                    recipient=Recipient(cpf=cpf),
                    card=Card(number=card_number),
                    hour_occurrence=hour_ocurrence,
                    store=Store(store_name=store_name, store_owner=store_owner)
                    )
            )
        return items

    def save(self, transaction: Transaction) -> bool:
        """This abstract function what defines what behavior should follow"""
        create_transaction ="""
            INSERT INTO transactions(
                id_type, date_occurrence, value, recipient_id, card_id, hour_occurrence, store_id)
            VALUES(%s,%s,%s,%s,%s,%s,%s);"""

        rst = self.db_postgres.execute(create_transaction, (
            transaction.type_transaction.id_type_transaction,
            transaction.date_occurrence,
            transaction.value,
            transaction.recipient.id_recipient,
            transaction.card.id_card,
            transaction.hour_occurrence,
            transaction.store.id_store
        ))

        if rst is not None:
            return False

        return True

    def get_all(self) -> list[Transaction]:
        '''Get all transactions'''
        transactions: list[Transaction] = list()
        get_transactions = """
            SELECT 
                t.id,tt.id_type,tt.description, tt.nature, tt.signal, t.date_occurrence, 
                t.value, r.id, r.cpf, c.id, c.card_number, t.hour_occurrence, 
                s.id,s.balance,s.store_name, s.store_owner
	        FROM public.transactions as t
            inner join recipient as r on r.id = t.recipient_id
            inner join card as c on c.id = t.card_id
            inner join store as s on s.id = t.store_id
            inner join type_transaction as tt on tt.id_type=t.id_type;
        """
        self.db_postgres.execute(get_transactions)
        for row in self.db_postgres.fetchall():
            transaction = Transaction(
                id_transaction=row[0],
                type_transaction=TypeTransaction(id_type_transaction=row[1],description=row[2],nature=row[3],signal=row[4]),
                date_occurrence=row[5],
                value=float(str(row[6])),
                recipient=Recipient(id_recipient=row[7],cpf=row[8]),
                card=Card(id_card=row[9], number=row[10]),
                hour_occurrence=row[11],
                store=Store(id_store=row[12], balance=float(str(row[13])), store_name=row[14], store_owner=row[15])
            )
            transactions.append(transaction)

        return transactions
