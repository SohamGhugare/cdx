import typer
from rich import print

app = typer.Typer()

@app.callback()
def callback():
    """ CDX - A powerful CLI application for aliasing your project paths """

@app.command(
    name="init",
    help="Initialize a cdx config"
)
def init():
    print("[yellow]Initializing a cdx config file...[/yellow]")
