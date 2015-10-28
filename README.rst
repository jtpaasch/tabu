Tabu
====

A tool for managing multiple projects.

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

At that point, you can make changes in ``~/code/tabu``, and you won't need to
 reinstall.


Component Directories
---------------------

Each component gets its own directory in the ``tabu/components`` folder::

    tabu/
      components/
        papi/
        platform/
        polaris/
        stem/


CLI Plugins
-----------

To add subcommands to the CLI, create a directory in your component directory
called ``cli``, and put files in there that define the CLI.

For instance, if you want to create a subcommand called ``foo``, you would
put a file called ``foo.py`` in a ``cli`` folder inside the foo component
folder, like this::

    tabu/
      components/
        foo/         <---- The component's folder.
          cli/       <---- CLI files go in here.
            foo.py   <---- A file that defines the ``foo`` subcommand.

Then you would define your ``foo`` subcommand inside that ``foo.py``
file. The CLI is based on Armin Rocher's ``click`` library. For more
on how to use the library to define your commands, see the documentation:
http://click.pocoo.org/5/ You can look at the ``system`` cli for examples
at ``tabu/system/cli/system.py``.

Last, you need to register your plugin with the main CLI. To do that, go
to the file ``ns/cli/main.py``, import your CLI module, and add it to the
``plugins`` dictionary, like this::

    from ns.components.foo.cli import foo
  
    plugins = {
        ...
        "foo": foo,
        }

Once you do that, the CLI will include your subcommand. You should see
it listed in the help::

    > tabu --help
    -->  ...
    -->  Commands:
    -->    foo  ...

Note: You may need to re-install the whole package to get the new CLI
subcommands, unless you've installed with the ``pip ... --editable`` flag.
