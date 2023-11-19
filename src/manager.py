from shelve import open
from classes import RefcauObjectArticle, RefcauObjectElectronic

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
        while self.enabled:
            self.sources()

    def sources(self) -> None:
        """
        This method lists all sources in the database.
        """
        with open(self.database) as database:
            keys = list(database.keys())
            keys.sort()
            for key in keys:
                print(database.get(key))


if __name__ == "__main__":
    RefcauManager("RefcauDatabase")
