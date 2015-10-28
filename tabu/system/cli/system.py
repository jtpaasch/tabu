# -*- coding: utf-8 -*-

"""A plugin command."""

import click


@click.group()
def system():
    """Control the system."""
    pass


@system.command()
def version():
    """Display the current version of the system."""
    click.echo("Version TBD.")
