from sprite import Sprite
from tile import Tile
from ability import Ability

from ability import TargetingType

class Wait(Ability):
    def __init__(self, name: str, potency: int, ap_cost: int, targeting_type: TargetingType, range: int, scene, user=None):
        super().__init__(name, potency, ap_cost, targeting_type, range, user=user)
        self.description = "Skip turn"
        self.scene = scene
    def activate(self):
        self.scene.current_character.action_points = self.scene.current_character.base_action_points
        self.scene.group_manager.determine_turn_queue()
        self.scene.current_character = self.scene.group_manager.get_next_character()
        self.scene.state_machine.change_state(self.scene.turn_state)
