from abc import ABC, abstractmethod
import datetime

from src.habit_tracker.domain.entities.completion import Completion
from src.habit_tracker.domain.entities.habit import Habit

class HabitRepository(ABC):
    @abstractmethod
    def create(self, habit: Habit) -> None:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Habit | None:
        pass

    @abstractmethod
    def get_all(self) -> list[Habit]:
        pass
    
    @abstractmethod
    def update(self, habit: Habit) -> None:
        pass
    
    @abstractmethod
    def delete(self, id: str) -> None:
        pass
    
    @abstractmethod
    def add_completion(self, habit_id: str, completed_at: datetime) -> None:
        pass
    
    @abstractmethod
    def get_completions(self, habit_id: str) -> list[Completion]:
        pass