from domain.ports.recipient import RepositoryRecipient
from domain.ports.card import RepositoryCard
from domain.ports.store import RepositoryStore
from domain.ports.types import RepositoryTypeTransaction
from domain.ports.transaction import RepositoryTransaction

from adapters.infrastructure.postgresql.recipient import RecipientImpl
from adapters.infrastructure.postgresql.card import CardImpl
from adapters.infrastructure.postgresql.store import StoreImpl
from adapters.infrastructure.postgresql.types import TypeTransactionImpl
from adapters.infrastructure.postgresql.transaction import TransactionImpl

from main import DB as POSTGRES_DB

def get_content_file(bts: bytes) -> str:
    """method get only content of bytes"""
    try:
        start_file = "text/plain\r\n\r\n"
        end_file = "\n\r\n"

        fist_block = bts.decode().split(start_file)
        block_content = "".join(fist_block[1]).split(end_file, maxsplit=1)[0]
    except IndexError:
        block_content = ""

    return block_content

def process_transaction(block: str) -> None:
    """Process file"""

    #Repository for Type Transaction
    repo_type = RepositoryTypeTransaction(TypeTransactionImpl(POSTGRES_DB))
    tp_transactions = repo_type.service_get_all()

    #Repository for Recipient
    repo_recipient = RepositoryRecipient(RecipientImpl(POSTGRES_DB))

    #Repository for Card
    repo_card = RepositoryCard(CardImpl(POSTGRES_DB))

    #Repository for Store
    repo_store = RepositoryStore(StoreImpl(POSTGRES_DB))

    #Repository for Transaction
    repo_trans = RepositoryTransaction(TransactionImpl(POSTGRES_DB))

    items = repo_trans.service_parse(tp_transactions, block)
    for item in items:
        repo_recipient.service_get_or_create(item.recipient)

        repo_card.service_get_or_create(item.card)

        repo_store.service_get_or_create(item.store)
        repo_store.service_update_balance(item)

        repo_trans.service_save(item)

def list_transaction()-> list:
    """Get all transactions."""
    repo_trans = RepositoryTransaction(TransactionImpl(POSTGRES_DB))
    return repo_trans.service_get_all()
