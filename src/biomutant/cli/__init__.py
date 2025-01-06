# SPDX-FileCopyrightText: 2025-present zeyus <dev@zeyus.com>
#
# SPDX-License-Identifier: MIT
import click

from biomutant.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="BioMutant")
def biomutant():
    click.echo("Hello world!")
