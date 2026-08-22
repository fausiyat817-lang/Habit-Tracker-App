import typer
from rich.console import Console

# Initialize main app and Rich console
app = typer.Typer(help="A CLI tool for managing tasks.")
console = Console()


if __name__ == "__main__":
    app()