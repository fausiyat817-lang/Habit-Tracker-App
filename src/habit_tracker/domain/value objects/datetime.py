import datetime
from dataclasses import dataclass


@dataclass
class DateTime:
    _dt: datetime

    def __init__(self, dt: datetime):
        self._dt = dt

    @property
    def value(self) -> datetime:
        return self._dt
    
    
    def __lt__(self, other):
        return self._dt < other._dt
    
    def __le__(self, other):
        return self._dt <= other._dt
    
    def __gt__(self, other):
        return self._dt > other._dt
    
    def __ge__(self, other):
        return self._dt >= other._dt
    
    
    def __eq__(self, other):
        if isinstance(other, DateTime):
            return self._dt == other._dt
        return False
    
    def __str__(self):
        return self._dt.isoformat()
    
    def __repr__(self):
        return f"DateTime({self._dt.isoformat()})"
    
    def __hash__(self):
        return hash(self._dt)
    
    