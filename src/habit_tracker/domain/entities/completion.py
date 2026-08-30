from dataclasses import dataclass
from ..value_objects.datetime import Datetime
from ..value_objects.id import Id


@dataclass
class Completion:
    habit_id: Id
    completed_at: Datetime