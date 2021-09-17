from attribute import Attribute
from stat_id import StatId

class StatCollection:

    def __init__(self):
        self.stat_dict = {}
    
    def add_to_dict(self, stat_id: StatId, stat: Attribute):
        self.stat_dict[stat_id] = stat

    def get_stat(self, stat_id: StatId):
        return self.stat_dict[stat_id]
    
    def print_stats(self):
        for key, value in self.stat_dict.items():
            print(f"{key}, {value.base_value}")
