from dataclasses import dataclass

@dataclass
class Card:
    """Class for keeping track of item in cards."""
    id_card : int
    number : str

    def __init__(self, number: str, id_card: int = None) -> None:
        self.id_card = id_card
        self.number = number
