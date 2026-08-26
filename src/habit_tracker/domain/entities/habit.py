from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class Periodicity(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

@dataclass
class Habit:
    id: str | None
    name: str
    description: str
    periodicity: Periodicity
    created_at: datetime
    
    def __init__(self, name: str, description: str, periodicity: Periodicity = Periodicity.DAILY):
        self.id = None
        self.name = name
        self.description = description
        self.periodicity = periodicity
        self.created_at = datetime.now()
    
    def is_valid_periodicity(self) -> bool:
        return self.periodicity in Periodicity
    
    def is_completed_in_period(self, completions, period_start: datetime, period_end: datetime) -> bool:
        for completion in completions:
            if period_start <= completion <= period_end:
                return True
        return False