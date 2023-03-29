from domain.entities.recipient import Recipient

class RecipientImpl:
    '''Recipient Interface Implementation'''
    cursor : any

    def __init__(self, cursor: any) -> None:
        self.cursor = cursor

    def get_or_create(self, recipient: Recipient) -> bool:
        '''description docstring'''
        get_recipient = """
            SELECT id, cpf FROM recipient WHERE cpf=%s;
        """
        create_recipient = """
            INSERT INTO recipient(cpf) VALUES(%s) RETURNING id;
        """
        self.cursor.execute(get_recipient, (recipient.cpf,))
        rst = self.cursor.fetchone()

        if rst:
            recipient.id_recipient = rst[0]
        else:
            self.cursor.execute(create_recipient, (recipient.cpf,))
            recipient.id_recipient = self.cursor.fetchone()[0]

        return True
