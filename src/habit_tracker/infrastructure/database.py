
import datetime
import sqlite3
from typing import override
from habit_tracker.domain.entities.completion import Completion
from sqlmodel import Enum, SQLModel, Field, Session, create_engine, select

from habit_tracker.domain.entities.habit import Habit, Periodicity 


sqlite_db = None

def init_sqlite_db(path: str):
    global sqlite_db
    sqlite_db = sqlite3.connect(path)
    
    
    
class CompletionModel(Completion, SQLModel, table=True):
    id: str | None = Field(default=None, primary_key=True)
    habit_id: str
    completed_at: datetime.datetime
    
    def to_domain(self) -> Completion:
        return Completion(
            id=self.id,
            habit_id=self.habit_id,
            completed_at=self.completed_at
        )


class PeriodicityModel(Enum, Periodicity):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    
    def to_domain(self) -> Periodicity:
        return Periodicity(self.value)

class HabitModel(Habit, SQLModel, table = True, ):
    id: str | None = Field(default=None, primary_key=True)
    name: str
    description: str
    periodicity: PeriodicityModel
    created_at: datetime
    completions: list[CompletionModel] = Field(default_factory=list, sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    
    def to_domain(self) -> Habit:
        return Habit(
            id=self.id, 
            name=self.name,
            description=self.description,
            periodicity=self.periodicity.to_domain(),
            created_at=self.created_at,
            completions=[completion.to_domain() for completion in self.completions]
        )
    
    



sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    

if __name__ == "__main__":
    create_db_and_tables()