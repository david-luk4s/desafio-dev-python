from domain.entities.card import Card

class CardImpl:
    '''Card Interface Implementation'''
    cursor : any

    def __init__(self, cursor: any) -> None:
        self.cursor = cursor

    def get_or_create(self, card: Card) -> bool:
        '''Try get or create card'''
        get_card = """
            SELECT id, card_number FROM card WHERE card_number=%s;
        """
        create_card = """
            INSERT INTO card(card_number) VALUES(%s) RETURNING id;
        """
        self.cursor.execute(get_card, (card.number,))
        rst = self.cursor.fetchone()

        if rst:
            card.id_card = rst[0]
        else:
            self.cursor.execute(create_card, (card.number,))
            card.id_card = self.cursor.fetchone()[0]

        return True
