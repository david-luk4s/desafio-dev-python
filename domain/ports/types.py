from abc import ABC, abstractmethod

from domain.entities.transaction import TypeTransaction

class TypeTransactionInterface(ABC):
    """Interface to define which type transaction contract should follow."""

    @classmethod
    @abstractmethod
    def save(cls, type_transaction: TypeTransaction) -> bool:
        """This abstract function what defines what behavior should follow"""

    @classmethod
    @abstractmethod
    def get_all(cls) -> dict[TypeTransaction]:
        """This abstract function what defines what behavior should follow"""


class RepositoryTypeTransaction:
    """Repository that receives any implementation of the transaction interface."""
    repos : TypeTransactionInterface

    def __init__(self, repos: TypeTransactionInterface) -> None:
        self.repos = repos

    def service_save(self, type_transaction: TypeTransaction) -> bool or Exception:
        """This function call calls the implementation that comes from the repository."""
        return self.repos.save(type_transaction)

    def service_get_all(self) -> dict[TypeTransaction]:
        """This function call calls the implementation that comes from the repository."""
        return self.repos.get_all()
