"""
This module defines the manager to hold sources.
"""

from shelve import open
from sources import (
    KierefSourceGeneric,
    KierefSourceType,
)

__date__ = "19/11/2023"
__author__ = "Jack Taylor"


class KierefManager:
    """
    This class is an object for managing sources.
    """

    def __init__(self, database: str) -> None:
        """
        This method initialises this manager and enables it by default.

        :param database: The database path
        :type database: str
        """
        self.enabled: bool = True
        self.database = database

    def print_references(self) -> None:
        """
        This method prints all sources in the database.
        """
        references = self.get_references()
        print(f"Sources: {len(references)}")
        for source in references:
            print(source)

    def get_references(self) -> list[KierefSourceGeneric]:
        """
        This method returns all sources in the database.
        """
        with open(self.database) as database:
            values = list(database.values())
            return values

    def add_reference(self, source: KierefSourceGeneric) -> None:
        """
        This method adds a new source to the database.

        :param source: The new source to add
        :type source: KierefSourceGeneric
        """
        with open(self.database) as database:
            database[source.id] = source

    def delete_reference(self, source: KierefSourceGeneric) -> None:
        """
        This method removes a source from the database.

        :param source: The source to delete
        :type source: KierefSourceGeneric
        """
        with open(self.database) as database:
            database.pop(source.id)

    def create_reference(self, reference_type: type[KierefSourceType]) -> None:
        """
        This method creates a source object based on the 'reference_type'
        parameter.

        :param reference_type: The type of reference to create
        :type reference_type: type[KierefObjectType]
        :return: The created reference object
        :rtype: KierefObjectType
        """
        new_reference = reference_type()
        self.add_reference(new_reference)
        return new_reference
