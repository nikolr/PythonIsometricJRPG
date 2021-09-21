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
        if self.scene.current_character.alive == False:
            print("Checking if current character is dead")
            self.scene.group_manager.remove_dead_characters()
            self.scene.group_manager.determine_turn_queue()
            self.scene.current_character = self.scene.group_manager.get_next_character()
        if self.scene.group_manager.dead_character_indicator == True:
            print("Flag dead character raised")
            if self.scene.group_manager.player_party_is_empty() == True or self.scene.group_manager.enemy_party_is_empty() == True:
                """Call win state or lose state"""
                pass
            self.scene.group_manager.remove_dead_characters()
            # self.scene.group_manager.determine_turn_queue()
            # self.scene.current_character = self.scene.group_manager.get_next_character()
        #Close character action panel
        # self.scene.state_machine.change_state()
        # Check for dead participants and remove them from the list. If len(player_participants) == 0 -> gameover state/scene 

        # print(self.scene.group_manager.participants)
        # self.scene.group_manager.remove_dead_characters()
        # print(self.scene.group_manager.participants)
        # if self.scene.group_manager.player_party_is_empty() == True or self.scene.group_manager.enemy_party_is_empty() == True:
        #     pass
        print("Exited Targeting State")
    def update(self):
        #Check for mouse hover over buttons
        pass

    def render(self):
        #Draw targeting tiles
        self.scene.selected_ability.draw_range_indicator(self.scene.disp, self.scene.current_character.sprite.tile)