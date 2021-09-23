from sprite import Sprite
from tile import Tile
from ability import Ability

from ability import TargetingType

class Move(Ability):
    def __init__(self, name: str, potency: int, ap_cost: int, targeting_type: TargetingType, range: int, user=None):
        super().__init__(name, potency, ap_cost, targeting_type, range, user=user)
        self.description = "Move 1 square forward"
    def action(self, character):
        character.sprite.move_a_square()
