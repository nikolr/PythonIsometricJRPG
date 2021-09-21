
from sprite import Sprite
from tile import Tile
from ability import Ability

from ability import TargetingType

class Move(Ability):
    def __init__(self, name, potency, ap_cost, range,targeting_type, user = None):
        super().__init__(name, potency, ap_cost, range, targeting_type, user)

    def action(self, character):
        character.sprite.move_a_square()
