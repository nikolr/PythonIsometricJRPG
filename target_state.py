from ability import Ability
from state import State
from director import Director
import pygame


class TargetState(State):
    """Keeps track of current character Action Points. After depletion or game end condition flags, get next state from queue? Or otherwise determine next state"""
    def __init__(self, director: Director, scene) -> None:
        State.__init__(self, director, )
        self.director = director
        self.scene = scene
        

    def enter(self):
        print("Entered Targeting State")

    def exit(self):
        #Close character action panel
        self.scene.state_machine.change_state()
    def update(self):
        #Check for mouse hover over buttons
        pass

    def render(self):
        #Draw targeting tiles
        self.scene.selected_ability.draw_range_indicator(self.scene.disp, self.scene.current_character.sprite.tile)