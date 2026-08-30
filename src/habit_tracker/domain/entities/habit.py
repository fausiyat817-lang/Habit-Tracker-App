from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from habit_tracker.domain.entities.completion import Completion
from ..value_objects.id import Id
from ..value_objects.datetime import Datetime
from ..value_objects.periodicity import Periodicity


@dataclass
class Habit:
    id: Id | None
    name: str
    description: str
    periodicity: Periodicity
    created_at: Datetime
    completions: list[Completion] = None
    
    def __init__(self, name: str, description: str, periodicity: Periodicity = Periodicity.DAILY):
        self.id = None
        self.name = name
        self.description = description
        self.periodicity = periodicity
        self.created_at = Datetime(datetime.now())
    
    def is_valid_periodicity(self) -> bool:
        return self.periodicity in Periodicity
    
    def is_completed_in_period(self, completions, period_start: Datetime, period_end: Datetime) -> bool:
        for completion in completions:
            if period_start <= completion <= period_end:
                return True
        return False