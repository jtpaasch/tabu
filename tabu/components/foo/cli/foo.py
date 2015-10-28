# -*- coding: utf-8 -*-

"""The ``foo`` subcommand."""

import click


@click.group()
def foo():
    """Manage the FOO component."""
    pass


@foo.command()
def version():
    """The current FOO version."""
    click.echo("Version TBD...")
