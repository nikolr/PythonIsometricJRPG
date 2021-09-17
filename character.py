from sprite import Sprite
from stat_collection import StatCollection

class Character:

    def __init__(self, name: str, stat_collection: StatCollection, sprite: Sprite, counter = 10):
        self.name = name
        self.stat_collection = stat_collection
        self.sprite = sprite
    
    def print_info(self):
        print(f"Name: {self.name}")
        self.stat_collection.print_stats()