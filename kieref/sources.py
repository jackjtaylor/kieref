"""
This module defines the classes used to create sources.
"""

from abc import ABC as AbstractBaseClass, abstractmethod
from dataclasses import dataclass
from typing import TypeVar
from uuid import uuid4

__date__ = "19/11/2023"
__author__ = "Jack Taylor"

KierefSourceType = TypeVar("KierefSourceType", bound="KierefSourceGeneric")


@dataclass
class KierefSourceAbstract(AbstractBaseClass):
    """
    This abstract dataclass is a base object for creating sources.
    """

    title: str
    creator: str
    date: str

    def __post_init__(self) -> None:
        """
        This method creates an identity after initialisation.
        """
        self.id = str(uuid4())

    @abstractmethod
    def reference(self) -> str:
        """
        This abstract method returns a reference based on the source.

        :return: The source reference
        :rtype: str
        """
        return f"{self.creator}, {self.title}. {self.date}."

    def cite(self) -> str:
        """
        This method returns a citation based on the source.

        :return: The source citation
        :rtype: str
        """
        return f"({self.creator}, {self.date})"

    def __repr__(self) -> str:
        """
        This method uses the source class type and 'cite()' function to
        represent its contents.

        :return: The reference of the object
        :rtype: str
        """
        return f"{self.__class__.__name__} {self.cite()}"


@dataclass
class KierefSourceElectronic(KierefSourceAbstract):
    """
    This dataclass is an object for creating electronic sources.
    """

    style: str
    site: str
    url: str
    accessed: str
    pages: str

    def reference(self) -> str:
        """
        This method returns a reference based on the electronic source.

        :return: The source reference
        :rtype: str
        """
        return (
            f"{self.creator}, {self.title}, {self.date} in: {self.site} ("
            f"{self.style} {self.url}), accessed on {self.accessed}, "
            f"{self.pages}."
        )

    def __repr__(self) -> str:
        """
        This function uses the parent class' '__repr__()' function to represent
        this source's data.
        """
        return super().__repr__()


@dataclass
class KierefSourceArticle(KierefSourceAbstract):
    """
    This dataclass is an object for creating article sources.
    """

    publisher: str
    volume: str
    pages: str

    def reference(self) -> str:
        """
        This method returns a reference based on the article source.

        :return: The source reference
        :rtype: str
        """
        return (
            f"{self.creator}, article. {self.title}, in: {self.publisher} "
            f"{self.volume}, {self.date}, {self.pages} pages."
        )

    def __repr__(self) -> str:
        """
        This function uses the parent class' '__repr__()' function to represent
        this source's data.
        """
        return super().__repr__()
