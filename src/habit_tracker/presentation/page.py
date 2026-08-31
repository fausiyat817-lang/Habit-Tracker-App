from abc import ABC, abstractmethod

from rich.color import name
from rich.console import Console


class CliPage(ABC):
    
    @abstractmethod
    def render(self) -> None:
        pass
    
    def handle_input(self, user_input: str) -> None:
        pass


class CliPageManager:
    
    pages: list[CliPage]
    
    def __init__(self, console: Console):
        self.pages = []
        self.add_page( MainPage(console))
        self.current_page = None

    def add_page(self, page: CliPage) -> None:
        self.pages.append(page)

    def set_current_page(self, page: CliPage) -> None:
        if page in self.pages:
            self.current_page = page
        else:
            raise ValueError(f"Page '{name}' does not exist.")
        
    

    def render_current_page(self) -> None:
        if self.current_page:
            self.current_page.render()
        else:
            raise ValueError("No current page set.")

    def handle_input(self, user_input: str) -> None:
        if self.current_page:
            self.current_page.handle_input(user_input)
        else:
            raise ValueError("No current page set.")
        

class MainPage(CliPage):
    
    def __init__(self, console: Console):
        super().__init__()
        self.console = console

    def render(self) -> None:
        self.console.print("Welcome to the Habit Tracker!")
        self.console.print("1. View Habits")
        self.console.print("2. Add Habit")
        self.console.print("3. Exit")

    def handle_input(self, user_input: str) -> None:
        if user_input == "1":
            self.console.print("Viewing habits...")
        elif user_input == "2":
            self.console.print("Adding a new habit...")
        elif user_input == "3":
            self.console.print("Exiting...")
        else:
            self.console.print("Invalid input. Please try again.")
            
            

class Prompts:
    
    def __init__(self, console: Console):
        self.console = console
        
    