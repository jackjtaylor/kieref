from shelve import open
from classes import RefcauObjectArticle, RefcauObjectElectronic, RefcauObjectGeneric

"""
This file defines the manager to hold references.
:author: Jack Taylor
:date: 19/11/2023
"""


class RefcauManager:
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

    def get_references(self) -> list[RefcauObjectGeneric]:
        """
        This method returns all sources in the database.
        """
        with open(self.database) as database:
            values = list(database.values())
            return values

    def add_reference(self, source: RefcauObjectGeneric) -> None:
        """
        This method adds a new source to the database.

        :param source: The new source to add
        :type source: RefcauObjectGeneric
        """
        with open(self.database) as database:
            database[source.uuid] = source

    def delete_reference(self, source: RefcauObjectGeneric) -> None:
        """
        This method removes a source from the database.

        :param source: The source to delete
        :type source: RefcauObjectGeneric
        """
        with open(self.database) as database:
            database.pop(source.uuid)


if __name__ == "__main__":
    RefcauManager("RefcauDatabase.db")
