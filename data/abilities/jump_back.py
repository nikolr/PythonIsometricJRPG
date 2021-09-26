from data.abilities.ability import Ability


#FIX
#Scene group manager

class JumpBack(Ability):
    def __init__(self, name: str, potency: int, ap_cost: int, targeting_type, range: int, user=None):
        super().__init__(name, potency, ap_cost, targeting_type, range, user=user)
        self.description = "Jump back 1 square"
    def activate(self):
        if self.user.sprite.move_backwards() == True:
            print("True")
            self.user.scene.current_character.action_points = self.user.scene.current_character.action_points - self.ap_cost
            if self.user.scene.current_character.action_points > 0:
                self.user.scene.state_machine.change_state(self.user.scene.turn_state)
            else:
                self.user.scene.end_turn()