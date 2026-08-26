import typer
from rich.console import Console

# Initialize main app and Rich console
app = typer.Typer(help="A CLI tool for managing tasks.")
console = Console()


@app.command()
def main(
    name: str = typer.Option(
        ..., prompt="Enter your name", help="Your name for personalized greetings"
    )
):
    console.print(f"[bold green]Welcome, {name}![/bold green]")
    # Additional logic for the CLI can be added here


if __name__ == "__main__":
    app()
