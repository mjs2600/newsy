import logging

import typer

from . import constants

app = typer.Typer()


@app.command()
def newsstand():
    typer.echo("Hello, World!")


def main():
    logging.basicConfig(level=constants.LOG_LEVEL)
    app()
