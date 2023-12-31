from dataclasses import asdict, fields
from shelve import open
from classes import (
    KierefObjectArticle,
    KierefObjectElectronic,
    KierefObjectGeneric,
    KierefObjectType,
)

"""
This file defines the manager to hold references.
:author: Jack Taylor
:date: 19/11/2023
"""


class KierefManager:
    """
    This class is an object for managing references.
    """

    def __init__(self, database: str) -> None:
        """
        This method initialises this object and enables the object.

        :param database: The database path
        :type database: str
        """
        self.enabled: bool = True
        self.database = database

    def print_references(self) -> None:
        """
        This method prints all references in the database.
        """
        references = self.get_references()
        print(f"There are currently {len(references)} references in the database.")
        for source in references:
            print(source)

    def get_references(self) -> list[KierefObjectGeneric]:
        """
        This method returns all sources in the database.
        """
        with open(self.database) as database:
            values = list(database.values())
            return values

    def add_reference(self, source: KierefObjectGeneric) -> None:
        """
        This method adds a new source to the database.

        :param source: The new source to add
        :type source: KierefObjectGeneric
        """
        with open(self.database) as database:
            database[source.uuid] = source

    def delete_reference(self, source: KierefObjectGeneric) -> None:
        """
        This method removes a source from the database.

        :param source: The source to delete
        :type source: KierefObjectGeneric
        """
        with open(self.database) as database:
            database.pop(source.uuid)

    def create_reference(self, type: type[KierefObjectType]) -> None:
        """
        This method creates a reference object by asking for input.

        :param type: The type of reference to create
        :type type: type[KierefObjectType]
        :return: The created reference object
        :rtype: KierefObjectType
        """
        pass


if __name__ == "__main__":
    KierefManager("KierefDatabase.db").print_references()
