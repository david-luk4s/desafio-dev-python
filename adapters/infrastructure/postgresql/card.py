from domain.entities.card import Card

class CardImpl:
    '''Card Interface Implementation'''
    db_postgres : any

    def __init__(self, db_postgres: any) -> None:
        self.db_postgres = db_postgres

    def get_or_create(self, card: Card) -> bool:
        '''Try get or create card'''
        get_card = """
            SELECT id, card_number FROM card WHERE card_number=%s;
        """
        create_card = """
            INSERT INTO card(card_number) VALUES(%s) RETURNING id;
        """
        self.db_postgres.execute(get_card, (card.number,))
        rst = self.db_postgres.fetchone()

        if rst:
            card.id_card = rst[0]
        else:
            self.db_postgres.execute(create_card, (card.number,))
            card.id_card = self.db_postgres.fetchone()[0]

        return True
