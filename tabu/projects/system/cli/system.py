# -*- coding: utf-8 -*-

"""The ``system`` subcommand."""

import click


@click.group()
def system():
    """Manage the SYSTEM."""
    pass


@system.command()
def version():
    """The current SYSTEM version."""
    click.echo("Version TBD...")
