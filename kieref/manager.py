"""
This module defines the manager to hold sources.
"""

from shelve import open
from sources import (
    KierefSourceAbstract,
    KierefSourceType,
)

__date__ = "19/11/2023"
__author__ = "Jack Taylor"


class KierefManager:
    """
    This class is an object for managing sources.
    """

    def __init__(self, database: str = "kieref.dbm") -> None:
        """
        This function initialises this manager and enables it by default.

        :param database: The database path
        :type database: str
        """
        self.enabled: bool = True
        self.database = database

    def print_sources(self) -> None:
        """
        This function prints all sources in the database.
        """
        references = self.get_sources()
        print(f"Sources: {len(references)}")
        for index, source in enumerate(references):
            print(f"{index + 1}: {source}")

    def get_source(self, index: int) -> KierefSourceType:
        """
        This function returns a source based on the given index.
        :param index: The index used
        :type index: int
        """
        with open(self.database) as database:
            keys = list(database.keys())
            source_id = keys[index + 1]
            return database[source_id]

    def get_sources(self) -> list[KierefSourceAbstract]:
        """
        This function returns all sources in the database.
        """
        with open(self.database) as database:
            values = list(database.values())
            return values

    def add_source(self, source: KierefSourceAbstract) -> None:
        """
        This function adds a new source to the database.

        :param source: The new source to add
        :type source: KierefSourceAbstract
        """
        with open(self.database) as database:
            database[source.id] = source

    def delete_source(self, source: KierefSourceAbstract) -> None:
        """
        This function removes a source from the database.

        :param source: The source to delete
        :type source: KierefSourceAbstract
        """
        with open(self.database) as database:
            database.pop(source.id)

    def create_source(self, reference_type: type[KierefSourceType]) -> None:
        """
        This function creates a source object based on the 'reference_type'
        parameter.

        :param reference_type: The type of reference to create
        :type reference_type: type[KierefObjectType]
        :return: The created reference object
        :rtype: KierefObjectType
        """
        new_reference = reference_type()
        self.add_source(new_reference)
        return new_reference
