class Recipient(object):
    ID : int
    CPF : str

    def __init__(self, id: int, cpf: str) -> None:
        self.ID = id
        self.CPF = cpf
