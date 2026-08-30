

from src.habit_tracker.domain.entities.completion import Completion
from src.habit_tracker.domain.entities.habit import Habit
from src.habit_tracker.domain.repositories.habit_repository import HabitRepository


class HabitService:
    def __init__(self, habit_repository: HabitRepository):
        self.habit_repository = habit_repository

    def create_habit(self, name: str, description: str, periodicity: str = "daily") -> Habit:
        
        if name is None or name.strip() == "":
            raise ValueError("Habit name cannot be empty.")
        
        if description is None or description.strip() == "":
            raise ValueError("Habit description cannot be empty.")
        
        if periodicity is None or periodicity.strip() == "":
            raise ValueError("Habit periodicity cannot be empty.")
        
        if periodicity not in ["daily", "weekly", "monthly"]:
            raise ValueError("Invalid periodicity. Must be 'daily', 'weekly', or 'monthly'.")
        
        habit = Habit(name=name, description=description, periodicity=periodicity)
        
        return  self.habit_repository.create(habit)


    def get_habit(self, habit_id: str) -> Habit | None:
        
        if habit_id is None or habit_id.strip() == "":
            raise ValueError("Habit ID cannot be empty.")
        
        return self.habit_repository.get_by_id(habit_id)
    
    def list_habits(self) -> list[Habit]:
        return self.habit_repository.get_all()

    def update_habit(self, habit_id: str, name=None, description=None, periodicity=None) -> Habit:
        
        if habit_id is None or habit_id.strip() == "":
            raise ValueError("Habit ID cannot be empty.")
        
        if name is not None and name.strip() == "":
            raise ValueError("Habit name cannot be empty.")
        
        if description is not None and description.strip() == "":
            raise ValueError("Habit description cannot be empty.")
        
        if periodicity is not None and periodicity.strip() == "":
            raise ValueError("Habit periodicity cannot be empty.")

        if periodicity is not None and periodicity not in ["daily", "weekly", "monthly"]:
            raise ValueError("Invalid periodicity. Must be 'daily', 'weekly', or 'monthly'.")
        
        habit = self.habit_repository.get_by_id(habit_id)
        
        if name is not None:
            habit.name = name
            
        if description is not None:
            habit.description = description
            
        if periodicity is not None :
            habit.periodicity = periodicity
            
        self.habit_repository.update(habit)
        return habit

    def delete_habit(self, habit_id: str) -> None:
        if habit_id is None or habit_id.strip() == "":
            raise ValueError("Habit ID cannot be empty.")
        
        self.habit_repository.delete(habit_id)
        
    def add_completion(self, habit_id: str, completed_at) -> None:
        if habit_id is None or habit_id.strip() == "":
            raise ValueError("Habit ID cannot be empty.")
        
        if completed_at is None:
            raise ValueError("Completion date cannot be empty.")
        
        if not isinstance(completed_at, (str, datetime.datetime)):
            raise ValueError("Completion date must be a string or a datetime object.")
        
        if isinstance(completed_at, str):
            try:
                completed_at = datetime.datetime.fromisoformat(completed_at)
            except ValueError:
                raise ValueError("Invalid date format. Use ISO format (YYYY-MM-DDTHH:MM:SS).")
            
        if completed_at > datetime.datetime.now():
            raise ValueError("Completion date cannot be in the future.")
         
        self.habit_repository.add_completion(habit_id, completed_at)
        
    def get_completions(self, habit_id: str) -> list[Completion]:
        if habit_id is None or habit_id.strip() == "":
            raise ValueError("Habit ID cannot be empty.")
        return self.habit_repository.get_completions(habit_id)