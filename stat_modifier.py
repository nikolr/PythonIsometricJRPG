from enum import Enum
from stat_id import StatId

class StatModType(Enum):
    FLAT = 1
    PERCENTADD = 2
    PERCENTMULTIPLY = 3

class StatModifier:

    def __init__(self, stat_mod_type: StatModType, stat_id: StatId, value: float, order: int, source = None):
        self.stat_mod_type = stat_mod_type
        self.stat_id = stat_id
        self.value = value
        self.order = order
        
