

import datetime
from typing import override

from sqlite3 import Connection as SQLiteConnection

from habit_tracker.domain.entities.completion import Completion
from habit_tracker.domain.entities.habit import Habit
from habit_tracker.domain.repositories.habit_repository import HabitRepository
from habit_tracker.infrastructure.database import CompletionModel, HabitModel
from sqlalchemy import Engine
from sqlmodel import Session, select




class SQLHabitRepository(HabitRepository):
    db_engine: Engine

    def __init__(self, db_engine: Engine):
        self.db_engine = db_engine

    
    @override
    def get_habit_by_id(self, id: str) -> Habit  | None:
        with Session(self.db_engine) as session:
            habit_model = session.get(HabitModel, id)
            if habit_model is None:
                return None
            return habit_model.to_domain()

    @override
    def get_all_habits(self) -> list[Habit]:
        with Session(self.db_engine) as session:
            habit_models = session.exec(select(HabitModel)).all()
            return [habit_model.to_domain() for habit_model in habit_models]

    @override
    def create_habit(self, habit: Habit) -> Habit:
        with Session(self.db_engine) as session:
            habit_model = HabitModel(**habit.dict())
            session.add(habit_model)
            session.commit()
            return habit_model.to_domain()
        self.db_connection.commit()
        return habit

    @override
    def delete_habit(self, habit: Habit) -> None:
        with Session(self.db_engine) as session:
            habit_model = session.get(HabitModel, habit.id)
            if habit_model:
                session.delete(habit_model)
                session.commit()

    @override
    def update_habit(self, habit: Habit) -> None:
        with Session(self.db_engine) as session:
            habit_model = session.get(HabitModel, habit.id)
            if habit_model:
                habit_model.name = habit.name
                habit_model.description = habit.description
                habit_model.periodicity = habit.periodicity
                session.commit()
        
    @override
    def add_completion(self, habit_id: str, completed_at: datetime) -> None:
        with Session(self.db_engine) as session:
            habit_model = session.get(HabitModel, habit_id)
            if habit_model:
                completion_model = CompletionModel(habit_id=habit_id, completed_at=completed_at)
                habit_model.completions.append(completion_model)
                session.commit()
        
    @override
    def get_completions(self, habit_id: str) -> list[Completion]:
        with Session(self.db_engine) as session:
            habit_model = session.get(HabitModel, habit_id)
            if habit_model:
                return [completion.to_domain() for completion in habit_model.completions]
            return []
