from dataclasses import dataclass
from datetime import datetime


@dataclass
class Completion:
    habit_id: str
    completed_at: datetime