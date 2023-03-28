from abc import ABC, abstractmethod

from domain.entities.store import Store
from domain.entities.transaction import Transaction

class StoreInterface(ABC):
    """Interface to define which store contract should follow."""

    @classmethod
    @abstractmethod
    def get_or_create(cls, store: Store) -> bool:
        """This abstract function what defines what behavior should follow"""

    @classmethod
    @abstractmethod
    def update_balance(cls, transaction: Transaction) -> None:
        """This abstract function what defines what behavior should follow"""


class RepositoryStore:
    """Repository that receives any implementation of the store interface."""
    repos : StoreInterface

    def __init__(self, repos: StoreInterface) -> None:
        self.repos = repos

    def service_get_or_create(self, store: Store) -> bool:
        """This function call calls the implementation that comes from the repository."""
        return self.repos.get_or_create(store)

    def service_update_balance(self, transaction: Transaction) -> None:
        """This function call calls the implementation that comes from the repository."""
        return self.repos.update_balance(transaction)
