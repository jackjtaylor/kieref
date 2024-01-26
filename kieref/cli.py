"""
This module is the text-based interface for Kieref.
"""

from click import group, argument, echo, option, prompt
from manager import KierefManager
from sources import KierefSourceElectronic, KierefSourceArticle

__date__ = "04/01/2024"
__author__ = "Jack Taylor"

manager = KierefManager()


@group("cli")
def cli() -> None:
    """
    This function is the main function of this module.

    When using the 'cli' group, this function will display help to the user.
    """
    pass


@cli.command()
def sources() -> None:
    """
    This function shows the user all sources in the database.
    """
    manager.print_sources()


@cli.command()
@option("--type", prompt="What source type do you want to create?")
def create(type: str) -> None:
    """
    This function creates a new source based on user input.
    """
    pass

@cli.command()
@argument('lang')
def language(lang) -> None:
    """
    This function changes the language interface.
    """
    echo("This application does not currently support other languages.")


if __name__ == "__main__":
    # This is the entry point of this module.
    cli()
