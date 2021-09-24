from sprite import Sprite
from tile import Tile
from ability import Ability

from ability import TargetingType

class Move(Ability):
    def __init__(self, name: str, potency: int, ap_cost: int, targeting_type: TargetingType, range: int, user=None):
        super().__init__(name, potency, ap_cost, targeting_type, range, user=user)
        self.description = "Move 1 square forward"
    def activate(self):
        if self.user.sprite.move_a_square() == True:
            self.user.scene.current_character.action_points = self.user.scene.current_character.action_points - self.ap_cost
            if self.user.scene.current_character.action_points > 0:
                self.user.scene.state_machine.change_state(self.user.scene.turn_state)
            else:
                print("Next turn")
                self.user.scene.current_character.action_points = self.user.scene.current_character.base_action_points
                self.group_manager.determine_turn_queue()
                self.user.scene.current_character = self.group_manager.get_next_character()
                self.state_machine.change_state(self.user.scene.turn_state)

