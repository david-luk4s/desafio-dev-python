from abc import ABC, abstractmethod

from domain.entities.card import Card

class CardInterface(ABC):
    """Interface to define which card contract should follow."""

    @classmethod
    @abstractmethod
    def get_or_create(cls, card: Card) -> bool:
        """This abstract function what defines what behavior should follow"""


class RepositoryCard:
    """Repository that receives any implementation of the card interface."""

    repos : CardInterface

    def __init__(self, repos: CardInterface) -> None:
        self.repos = repos

    def service_get_or_create(self, card: Card) -> bool:
        """This function call calls the implementation that comes from the repository."""
        return self.repos.get_or_create(card)
