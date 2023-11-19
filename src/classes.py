from abc import ABC as AbstractBaseClass, abstractmethod
from dataclasses import dataclass
from typing import override

"""
This file defines the classes used to create references.
@author Jack Taylor
@date 19/11/2023
"""


@dataclass
class RefcauObjectGeneric(AbstractBaseClass):
    """
    This abstract dataclass is a base object for creating references.
    """

    name: str
    creator: str
    date: int

    @abstractmethod
    def reference(self) -> str:
        """
        This abstract method returns a reference based on the object.

        :return: The source reference
        :rtype: str
        """
        return f"{self.creator}, {self.name}. {self.date}."

    def cite(self) -> str:
        """
        This method returns a citation based on the object.

        :return: The source citation
        :rtype: str
        """
        return f"({self.creator}, {self.date})"


@dataclass
class RefcauObjectElectronic(RefcauObjectGeneric):
    """
    This dataclass is an object for creating electronic source references.
    """

    style: str
    site: str
    url: str
    accessed: str
    pages: int

    @override
    def reference(self) -> str:
        """
        This method returns a reference based on the electronic source.

        :return: The source reference
        :rtype: str
        """
        return f"{self.creator}, {self.name}, {self.pages} seiten, in: {self.site} ({self.url}), abgerufen am {self.accessed}."


@dataclass
class RefcauObjectArticle(RefcauObjectGeneric):
    """
    This dataclass is an object for creating article source references.
    """

    publisher: str
    volume: str
    pages: int

    @override
    def reference(self) -> str:
        """
        This method returns a reference based on the article source.

        :return: The source reference
        :rtype: str
        """
        return f"{self.creator}, Art. {self.name}, in: {self.publisher} {self.volume}, {self.date}, {self.pages}."
