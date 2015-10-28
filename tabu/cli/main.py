# -*- coding: utf-8 -*-

"""The ``cli`` module.

This module initializes the main CLI. The CLI is a plugin-based
command line module, meaning that it loads all its subcommands from
directories. The directories it loads its plugins from are
stipulated in the ``plugins`` dictionary below.

"""

from ns.cli.plugincli import PluginCli

from ns.components.foo.cli import foo
from ns.system.cli import system

plugins = {
    "system": system,
    "foo": foo,
    }

cli = PluginCli(
    name="ns",
    help="Manage multiple projects.",
    plugins=plugins
    )
