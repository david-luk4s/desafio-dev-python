from dataclasses import dataclass

@dataclass
class Recipient:
    """Class for keeping track item of recipients."""
    id_recipient : int
    cpf : str

    def __init__(self, cpf: str, id_recipient: int = None) -> None:
        self.id_recipient = id_recipient
        self.cpf = cpf
