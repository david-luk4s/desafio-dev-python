from abc import ABC, abstractmethod

from domain.entities.recipient import Recipient

class RecipientInterface(ABC):
    """Interface to define which recipient contract should follow."""

    @classmethod
    @abstractmethod
    def get_or_create(cls, recipient: Recipient) -> bool:
        """This abstract function what defines what behavior should follow"""


class RepositoryRecipient(object):
    """Repository that receives any implementation of the store interface."""
    repos : RecipientInterface

    def __init__(self, repos: RecipientInterface) -> None:
        self.repos = repos

    def service_get_or_create(self, recipient: Recipient) -> bool:
        """This function call calls the implementation that comes from the repository."""
        return self.repos.get_or_create(recipient)
