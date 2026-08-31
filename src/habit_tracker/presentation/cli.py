
from typer import Typer
from rich.console import Console


app = Typer(name="habit-tracker", help="A CLI application for tracking habits.")
_console = Console()

@app.command()
def _main():
    """Entry point for the habit tracker CLI application."""
    _console.print("[bold green]Welcome to the Habit Tracker CLI![/bold green]")
    
    
    