from domain.entities.transaction import TypeTransaction
from domain.ports.transaction import RepositoryTransaction
from adapters.infrastructure.postgresql.transaction import TransactionImpl


def test_length_cnab_file():
    """Test length of cnab file"""
    f = open(file="CNAB.txt", mode="r", encoding="utf-8")
    block = f.read().splitlines()
    assert len(block) == 21


def test_process_transactions():
    """Test process transactions."""
    block = open(file="CNAB.txt", mode="r", encoding="utf-8")
    type_transactions: dict[TypeTransaction] = dict()

    type_transactions[1] = TypeTransaction(1, 'Débito', 'Entrada', '+')
    type_transactions[2] = TypeTransaction(2, 'Boleto', 'Saída', '-')
    type_transactions[3] = TypeTransaction(3, 'Financiamento', 'Saída', '-')
    type_transactions[4] = TypeTransaction(4, 'Crédito', 'Entrada', '+')
    type_transactions[5] = TypeTransaction(5, 'Recebimento Empréstimo', 'Entrada', '+')
    type_transactions[6] = TypeTransaction(6, 'Vendas', 'Entrada', '+')
    type_transactions[7] = TypeTransaction(7, 'Recebimento TED', 'Entrada', '+')
    type_transactions[8] = TypeTransaction(8, 'Recebimento DOC', 'Entrada', '+')
    type_transactions[9] = TypeTransaction(9, 'Aluguel', 'Saída', '-')

    repo = RepositoryTransaction(TransactionImpl(...))
    items = repo.service_parse(type_transactions, block.read())

    assert len(items) == 21

    for item in items:
        assert len(item.recipient.cpf) == 11

        assert len(item.card.number) == 12

        assert len(item.store.store_owner) == 14

        assert len(item.store.store_name) >= 18
