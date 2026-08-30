from dataclasses import dataclass
from uuid import uuid4

@dataclass
class Id:
    value: str

    def __init__(self):
        self.value = str(uuid4())

    def __str__(self):
        return self.value
    
    def __eq__(self, other):
        if isinstance(other, Id):
            return self.value == other.value
        return False
    
    def __hash__(self):
        return hash(self.value)
    
    def __repr__(self):
        return f"Id({self.value})"
    
    def __lt__(self, other):
        if isinstance(other, Id):
            return self.value < other.value
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Id):
            return self.value <= other.value
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Id):
            return self.value > other.value
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Id):
            return self.value >= other.value
        return NotImplemented   