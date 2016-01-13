# -*- coding: utf-8 -*-

"""The main ``cli`` module.

This module initializes a plugin-based CLI. The CLI is plugin-based
in the sense that all subcommands are defined in other modules, and
those are loaded into this one. The subcommand modules to load should
be specified in the ``plugins`` dictionary below.

"""

# This module initialize a CLI and loads any specified plugins.
from tabu.utils.cli.plugincli import PluginCli

# Import any plugin modules you want the CLI to load here:
from tabu.projects.foo.cli import foo
from tabu.projects.system.cli import system

# Now define the plugins you want the CLI to load.
# Each key/value pairs should be in this format::
#
#     "<subcommand-name>": <module-that-implements-that-subcommand>
#
# For example, if you have a module ``tabu.projects.foo.cli.foo.py``
# that implements a subcommand called "foo", import the module and
# then add it to the ``plugins`` dictionary like this::
#
#     import tabu.projects.foo.cli.foo
#
#     plugins = {
#         ...
#         "foo": foo,
#         }
#
plugins = {
    "system": system,
    "foo": foo,
    }

description = "Manage multiple projects."
cli = PluginCli(name="tabu", help=description, plugins=plugins)
