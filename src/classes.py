from abc import ABC as AbstractBaseClass, abstractmethod
from dataclasses import dataclass
from uuid import uuid4
from typing import TypeVar

"""
This file defines the classes used to create references.
:author: Jack Taylor
:date: 19/11/2023
"""

"""
This TypeVar defines a generic type for RefcauObjects.
"""
RefcauObjectType = TypeVar("RefcauObjectType")


@dataclass
class RefcauObjectGeneric(AbstractBaseClass):
    """
    This abstract dataclass is a base object for creating references.
    """

    title: str
    creator: str
    date: str
    uuid: str

    def __init__(self) -> None:
        """
        This method initialises this object and creates a UUID.
        """
        self.uuid = str(uuid4())

    @abstractmethod
    def reference(self) -> str:
        """
        This abstract method returns a reference based on the object.

        :return: The source reference
        :rtype: str
        """
        return f"{self.creator}, {self.title}. {self.date}."

    def cite(self) -> str:
        """
        This method returns a citation based on the object.

        :return: The source citation
        :rtype: str
        """
        return f"({self.creator}, {self.date})"

    def __repr__(self) -> str:
        """
        This method uses the object's reference() method to print its data.

        :return: The reference of the object
        :rtype: str
        """
        return self.reference()


@dataclass
class RefcauObjectElectronic(RefcauObjectGeneric):
    """
    This dataclass is an object for creating electronic source references.
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
        return f"{self.creator}, {self.title}, {self.date} in: {self.site} ({self.style} {self.url}), abgerufen am {self.accessed}, {self.pages}."


@dataclass
class RefcauObjectArticle(RefcauObjectGeneric):
    """
    This dataclass is an object for creating article source references.
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
        return f"{self.creator}, Art. {self.title}, in: {self.publisher} {self.volume}, {self.date}, {self.pages} seiten."
