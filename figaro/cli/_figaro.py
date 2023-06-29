"""Command line interface for Jobrunner"""

# Standard libraries
import subprocess
import pkg_resources

# Feature libraries
import click


@click.group(name="figaro", invoke_without_command=True)
@click.pass_context
@click.option("--version", "-v", is_flag=True)
def figaro(ctx, version):
    """
    \b
    Command line tool to organize and manage computing jobs.
    """
    if ctx.invoked_subcommand is None and not version:
        subprocess.run(
            "export PATH=~/.local/bin:/usr/local/bin:$PATH && figaro --help",
            shell=True,
            check=True,
        )

    if version:
        click.echo(pkg_resources.require("figaro")[0].version)
