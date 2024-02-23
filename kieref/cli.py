"""
This module is the text-based interface for Kieref.
"""
from click import group, argument, echo, option
from dataclasses import fields

from manager import KierefManager
from sources import KierefSourceArticle, KierefSourceElectronic, KierefSourceType

__date__ = "04/01/2024"
__author__ = "Jack Taylor"

manager = KierefManager()
types: dict[str, KierefSourceType] = {
    "article": KierefSourceArticle,
    "electronic": KierefSourceElectronic,
}


@group("cli")
def cli() -> None:
    """
    This application lets users create and manage sources.
    """
    pass


@cli.command()
def sources() -> None:
    """
    This function shows the user all sources in the database.
    """
    manager.print_sources()


@cli.command()
@option("--index", prompt="What index do you want to get?", type=int, required=True)
def get(index: int) -> None:
    """
    This function gets a source based on its index.
    """
    source = manager.get_source(index)
    print(f"Source {index}:")
    print(f"Cite: {source.cite()}")
    print(f"Reference: {source.reference()}")


@cli.command()
@option("--index", prompt="What index do you want to delete?", type=int, required=True)
def delete(index: int) -> None:
    """
    This function deletes a source based on its index.
    """
    source = manager.get_source(index)
    manager.delete_source(source)
    print("The source was deleted.")


@cli.command()
@option("--type", prompt="What source type do you want to create?")
def create(type: str) -> None:
    """
    This function creates a new source based on user input.
    """
    type = type.strip().lower()

    if type in types:
        vars = {}
        for field in fields(types[type]):
            vars[field.name] = input(f"{field.name.capitalize()}: ")
        source = types[type](**vars)
        manager.add_source(source)
        print(f"The source {source.title} was added.")
        print(f"{source.id}")
    else:
        print("Invalid source type.")


@cli.command()
@argument("lang")
def language(lang) -> None:
    """
    This function changes the language interface.
    """
    echo("This application does not currently support other languages.")


if __name__ == "__main__":
    # This is the entry point of this module.
    cli()
