from data.tile import Tile
from data.abilities.ability import Ability

class Face(Ability):
    def __init__(self, name: str, potency: int, ap_cost: int, targeting_type, range: int, user=None):
        super().__init__(name, potency, ap_cost, targeting_type, range, user=user)
        self.description = "Turn around"
    def action(self, target_tile: Tile):
        self.user.sprite.set_facing(target_tile)
