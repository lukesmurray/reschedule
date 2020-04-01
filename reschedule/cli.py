"""Console commands for the scheduler."""
from __future__ import print_function
from .config import task_file_path
from .task_parser import TaskParser
from .scheduler import schedule_tasks
import typer


app = typer.Typer()


@app.command()
def run():
    """Run the scheduler.

    This command is exported as the script for the package.
    """
    tasks = TaskParser().get_tasks(task_file_path)
    schedule_tasks(tasks)


@app.command()
def config():
    """View, update, or edit the reschedule config file.
    """
    typer.echo("not implemented yet")


@app.command()
def login():
    """Login or change google calendar accounts.
    """
    typer.echo("not implemented yet")


def main():
    app()


if __name__ == "__main__":
    main()
