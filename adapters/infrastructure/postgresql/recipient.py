from domain.entities.recipient import Recipient

class RecipientImpl:
    '''Recipient Interface Implementation'''
    db_postgres : any

    def __init__(self, db_postgres: any) -> None:
        self.db_postgres = db_postgres

    def get_or_create(self, recipient: Recipient) -> bool:
        '''description docstring'''
        get_recipient = """
            SELECT id, cpf FROM recipient WHERE cpf=%s;
        """
        create_recipient = """
            INSERT INTO recipient(cpf) VALUES(%s) RETURNING id;
        """
        self.db_postgres.execute(get_recipient, (recipient.cpf,))
        rst = self.db_postgres.fetchone()

        if rst:
            recipient.id_recipient = rst[0]
        else:
            self.db_postgres.execute(create_recipient, (recipient.cpf,))
            recipient.id_recipient = self.db_postgres.fetchone()[0]

        return True
