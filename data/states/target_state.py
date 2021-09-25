from data.scenes.defeat import Defeat
import data.scenes.win 
from data.states.state import State
import pygame



class TargetState(State):
    """Keeps track of current character Action Points. After depletion or game end condition flags, get next state from queue? Or otherwise determine next state"""
    def __init__(self, director, scene) -> None:
        State.__init__(self, director)
        self.director = director
        self.scene = scene

        self.ability_info_panel = pygame.Rect([director.screen.get_rect().topleft[0] + 200, director.screen.get_rect().topleft[1], 600, 200])


        self.font = pygame.font.Font("resources/font/PressStart2P-vaV7.ttf", 15)

        

    def enter(self):
        print("Entered Targeting State")

    def exit(self):
        if self.scene.group_manager.dead_character_indicator == True:
            self.scene.group_manager.remove_dead_characters()
            if self.scene.current_character.alive == False:
                print("Checking if current character is dead")
                # self.scene.group_manager.remove_dead_characters()
                self.scene.group_manager.determine_turn_queue()
                self.scene.current_character = self.scene.group_manager.get_next_character()
            
            print("Flag dead character raised")
            # self.scene.group_manager.remove_dead_characters()
            if self.scene.group_manager.player_party_is_empty() == True:
                self.director.change_scene(Defeat(self.director))
            elif self.scene.group_manager.enemy_party_is_empty() == True:
                """Call win state or lose state"""
                self.director.change_scene(data.scenes.win.Win(self.director))
            

        #Update sprite positions
        self.scene.group_manager.player_sprites = [c.sprite.pos for c in self.scene.group_manager.player_party]
        # self.scene.group_manager.enemy_sprites = [c.sprite.pos for c in self.scene.group_manager.enemy_party]
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

        #Draw info panel
        pygame.draw.rect(self.director.screen,(100, 100, 100), self.ability_info_panel)

        #Blit description
        self.director.screen.blit(self.font.render(f"{self.scene.selected_ability.name}:", True, (255, 255, 255)), (self.director.screen.get_rect().topleft[0] + 200, self.director.screen.get_rect().topleft[1]))
        blitlines(self.scene.director.screen, self.scene.selected_ability.description, self.font, (255, 255, 255), (self.director.screen.get_rect().topleft[0] + 200), self.director.screen.get_rect().topleft[1] + 20)
        
        self.director.screen.blit(self.font.render(f"Damage: {self.scene.selected_ability.potency}", True, (255, 255, 255)), (self.director.screen.get_rect().topleft[0] + 200, self.director.screen.get_rect().topleft[1] + 60))
        self.director.screen.blit(self.font.render(f"AP cost: {self.scene.selected_ability.ap_cost}", True, (255, 255, 255)), (self.director.screen.get_rect().topleft[0] + 200, self.director.screen.get_rect().topleft[1] + 80))

def blitlines(surf, text, renderer, color, x, y):
    h = renderer.get_height()
    lines = text.split('\n')
    for i, ll in enumerate(lines):
        txt_surface = renderer.render(ll, True, color)
        surf.blit(txt_surface, (x, y+(i*h)))
