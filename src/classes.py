from abc import ABC as AbstractBaseClass, abstractmethod
from dataclasses import dataclass

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
    location: str
    accessed: str
    pages: int

    def reference(self) -> str:
        """
        This method returns a reference based on the electronic source.

        :return: The source reference
        :rtype: str
        """
        return f"{self.creator}, {self.name}. {self.date}, {self.location}, {self.accessed}, {self.pages}."
