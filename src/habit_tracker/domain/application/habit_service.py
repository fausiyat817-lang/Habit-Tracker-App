

from src.habit_tracker.domain.entities.completion import Completion
from src.habit_tracker.domain.entities.habit import Habit
from src.habit_tracker.domain.repositories.habit_repository import HabitRepository


class HabitService:
    def __init__(self, habit_repository: HabitRepository):
        self.habit_repository = habit_repository

    def create_habit(self, name: str, description: str, periodicity: str = "daily") -> Habit:
        habit = Habit(name=name, description=description, periodicity=periodicity)
        self.habit_repository.create(habit)
        return habit

    def get_habit(self, habit_id: str) -> Habit | None:
        return self.habit_repository.get_by_id(habit_id)
    
    def list_habits(self) -> list[Habit]:
        return self.habit_repository.get_all()

    def update_habit(self, habit_id: str, name=None, description=None, periodicity=None) -> Habit:
        habit = self.habit_repository.get_by_id(habit_id)
        if name:
            habit.name = name
        if description:
            habit.description = description
        if periodicity:
            habit.periodicity = periodicity
        self.habit_repository.update(habit)
        return habit

    def delete_habit(self, habit_id: str) -> None:
        self.habit_repository.delete(habit_id)
        
    def add_completion(self, habit_id: str, completed_at) -> None:
        self.habit_repository.add_completion(habit_id, completed_at)
        
    def get_completions(self, habit_id: str) -> list[Completion]:
        return self.habit_repository.get_completions(habit_id)