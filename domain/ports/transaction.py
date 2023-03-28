from abc import ABC, abstractmethod

from domain.entities.transaction import TypeTransaction, Transaction

class TransactionInterface(ABC):
    """Interface to define which card contract should follow."""

    @classmethod
    @abstractmethod
    def parse(cls, type_transaction: dict[TypeTransaction], block: str) -> list[Transaction]:
        """This abstract function what defines what behavior should follow"""

    @classmethod
    @abstractmethod
    def save(cls, transaction: Transaction) -> bool:
        """This abstract function what defines what behavior should follow"""

    @classmethod
    @abstractmethod
    def get_all(cls) -> list[Transaction]:
        """This abstract function what defines what behavior should follow"""


class RepositoryTransaction:
    """Repository that receives any implementation of the transaction interface."""
    repos : TransactionInterface

    def __init__(self, repos: TransactionInterface) -> None:
        self.repos = repos

    def service_parse(self, type_transaction: dict[TypeTransaction], block: str) -> list[Transaction]:
        """This function call calls the implementation that comes from the repository."""
        return self.repos.parse(type_transaction, block)

    def service_save(self, transaction: Transaction) -> bool:
        """This function call calls the implementation that comes from the repository."""
        return self.repos.save(transaction)

    def service_get_all(self) -> list[Transaction]:
        """This function call calls the implementation that comes from the repository."""
        return self.repos.get_all()
