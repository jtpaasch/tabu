Tabu
====

A tool for managing multiple projects.


All the projects together are a ``system``, and each project is a ``component``
of the system.

The name comes from the Tabu Cocktail, listed in Trader Vic's *Bartender's Guide*.


Installation
------------

Use pip::

    > pip install tabu

Installation for Development
----------------------------

if you want to do any development with the repo, put it somewhere on your system,
e.g., in a folder at ``~/code/tabu``.

Then, you can install it with pip, but using the ``editable`` flag::

    > pip install ~/code/tabu --editable


Usage
-----

From a terminal, use the command line tool. For instance, to see the help::

    > tabu --help

Use the ``--help`` flag to puruse other commands too, e.g.::

   > tabu system --help


System Directory
----------------

Data and code regarding the system as a whole is kept in its own directory::

    tabu/
        system/  <---- System-wide files go in here.
    

Component Directories
---------------------

Each component gets its own directory in the ``tabu/components`` folder. If
``foo`` and ``bar`` are separate components, it would look something like this::

    tabu/
        components/
            foo/
            bar/


Where to put CLI plugins
------------------------

To add subcommands to the CLI for a component, create a directory in your
component directory called ``cli``, and put files in there that define the CLI.

For instance, if you want to create a subcommand called ``foo``, you would
put a file called ``foo.py`` in a ``cli`` folder inside the component's
folder, like this::

    tabu/
        components/
            foo/            <---- The component's folder.
                cli/        <---- CLI files go in here.
                    foo.py  <---- Defines the ``foo`` subcommand.

Then you would define your ``foo`` subcommand inside that ``foo.py``
file.

The CLI is based on Armin Ronacher's ``click`` library. For more
on how to use the library to define your commands, see the documentation:
http://click.pocoo.org/5/.

You can also look at the ``system`` cli for examples
at ``tabu/system/cli/system.py``.


Registering CLI plugins
-----------------------

Once you have CLI plugin code written, you need to register your plugin with the
main CLI. To do that, go to the file ``tabu/cli/main.py``, import your CLI module,
and add it to the ``plugins`` dictionary, like this::

    from tabu.components.foo.cli import foo
  
    plugins = {
        ...
        "foo": foo,
        }

That tells the CLI to include your subcommand. You can then see it listed
in the help::

    > tabu --help
    --   ...
    --   Commands:
    --     foo  ...

Note: You may need to re-install the whole package to get the new CLI
subcommands, unless you've installed with the ``pip ... --editable`` flag.
