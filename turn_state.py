from attribute_id import AttributeId
import pygame
from state import State
from director import Director
from button import Button


class TurnState(State):
    """Keeps track of current character Action Points. After depletion or game end condition flags, get next state from queue? Or otherwise determine next state"""

    

    def __init__(self, director: Director, scene) -> None:
        State.__init__(self, director)
        self.director = director
        self.scene = scene

        self.ability_buttons = {}

        self.hovered_ability = None

        self.ability_panel = pygame.Rect([director.screen.get_rect().midleft[0], director.screen.get_rect().midleft[1] + 280, 450, 200])
        self.name_panel = pygame.Rect([director.screen.get_rect().midleft[0], director.screen.get_rect().midleft[1] + 280, 225, 50])
        self.ap_panel = pygame.Rect([director.screen.get_rect().midleft[0] + 225, director.screen.get_rect().midleft[1] + 280, 225, 50])

        self.first_player_panel = pygame.Rect([director.screen.get_rect().midleft[0], director.screen.get_rect().midleft[1] - 150, 225, 125])
        self.second_player_panel = pygame.Rect([director.screen.get_rect().midleft[0], director.screen.get_rect().midleft[1]  - 25, 225, 125])
        self.third_player_panel = pygame.Rect([director.screen.get_rect().midleft[0], director.screen.get_rect().midleft[1] + 100, 225, 125])

        self.player_info_panel = pygame.Rect([director.screen.get_rect().midleft[0], director.screen.get_rect().midleft[1] - 150, 225, 375])
        self.font = pygame.font.Font("font/PressStart2P-vaV7.ttf", 25)

    def enter(self):
        print("Entered Turn State")
        self.ability_buttons.clear()
        for i in range(len(self.scene.current_character.abilities)):
            # self.ability_buttons.append(Button((0,0,70), self.director.screen.get_rect().midleft[0], self.director.screen.get_rect().midleft[1] + 300 + (i + 20), 100, 50, ab))
            # self.ability_buttons[f"{i}"] = self.scene.current_character.abilities[i]
            self.ability_buttons[f"{i}"] = Button((0,0,70), self.director.screen.get_rect().midleft[0], self.director.screen.get_rect().midleft[1] + 330 + (i * 30), 100, 35, self.scene.current_character.abilities[i])
        # if self.scene.group_manager.dead_character_indicator == True:
        #     if self.scene.group_manager.player_party_is_empty() == True or self.scene.group_manager.enemy_party_is_empty() == True:
        #         """Call win state or lose state"""
        #         pass
        #     self.scene.group_manager.remove_dead_characters()
        #     self.scene.group_manager.determine_turn_queue()
    def exit(self):
        # if self.scene.current_character.alive == False:
        #     self.scene.current_character = self.scene.group_manager.get_next_character()

        # if self.scene.group_manager.dead_character_indicator == True:
        #     if self.scene.group_manager.player_party_is_empty() == True or self.scene.group_manager.enemy_party_is_empty() == True:
        #         """Call win state or lose state"""
        #         pass
        #     self.scene.group_manager.remove_dead_characters()
        #     self.scene.group_manager.determine_turn_queue()
        #     self.scene.current_character = self.scene.group_manager.get_next_character()
        # print("Exited Turn State")
        pass
    def update(self):
        for btn in self.ability_buttons.values():
            if btn.isOver((self.scene.x_world, self.scene.y_world)):
                self.hovered_ability = btn.ability



    def render(self):
        pygame.draw.rect(self.director.screen,(100, 100, 100), self.ability_panel)

        pygame.draw.rect(self.director.screen,(100, 100, 100), self.player_info_panel)

        pygame.draw.rect(self.director.screen,(0, 0, 0), self.first_player_panel, 3)
        pygame.draw.rect(self.director.screen,(0, 0, 0), self.second_player_panel, 3)
        pygame.draw.rect(self.director.screen,(0, 0, 0), self.third_player_panel, 3)

        pygame.draw.rect(self.director.screen,(0, 0, 0), self.name_panel, 3)
        pygame.draw.rect(self.director.screen,(0, 0, 0), self.ap_panel, 3)

        self.director.screen.blit(self.font.render(self.scene.group_manager.player_party[0].name, True, (255, 255, 255)), (self.director.screen.get_rect().midleft[0] + 5, self.director.screen.get_rect().midleft[1] - 145))
        self.director.screen.blit(self.font.render(str(self.scene.group_manager.player_party[0].get_attribute_value(AttributeId.HP)), True, (255, 255, 255)), (self.director.screen.get_rect().midleft[0] + 5, self.director.screen.get_rect().midleft[1] - 120))
        self.director.screen.blit(self.font.render(str(self.scene.group_manager.player_party[0].counter), True, (255, 255, 255)), (self.director.screen.get_rect().midleft[0] + 5, self.director.screen.get_rect().midleft[1] - 95))

        self.director.screen.blit(self.font.render(self.scene.group_manager.player_party[1].name, True, (255, 255, 255)), (self.director.screen.get_rect().midleft[0] + 5, self.director.screen.get_rect().midleft[1] - 25))
        self.director.screen.blit(self.font.render(str(self.scene.group_manager.player_party[1].get_attribute_value(AttributeId.HP)), True, (255, 255, 255)), (self.director.screen.get_rect().midleft[0] + 5, self.director.screen.get_rect().midleft[1]))
        self.director.screen.blit(self.font.render(str(self.scene.group_manager.player_party[1].counter), True, (255, 255, 255)), (self.director.screen.get_rect().midleft[0] + 5, self.director.screen.get_rect().midleft[1] + 25))

        self.director.screen.blit(self.font.render(self.scene.group_manager.player_party[2].name, True, (255, 255, 255)), (self.director.screen.get_rect().midleft[0] + 5, self.director.screen.get_rect().midleft[1] + 100))
        self.director.screen.blit(self.font.render(str(self.scene.group_manager.player_party[2].get_attribute_value(AttributeId.HP)), True, (255, 255, 255)), (self.director.screen.get_rect().midleft[0] + 5, self.director.screen.get_rect().midleft[1] + 125))
        self.director.screen.blit(self.font.render(str(self.scene.group_manager.player_party[2].counter), True, (255, 255, 255)), (self.director.screen.get_rect().midleft[0] + 5, self.director.screen.get_rect().midleft[1] + 150))

        self.director.screen.blit(self.font.render(self.scene.current_character.name, True, (255, 255, 255)), (self.director.screen.get_rect().midleft[0], self.director.screen.get_rect().midleft[1] + 290))
        self.director.screen.blit(self.font.render(f"AP: {self.scene.current_character.action_points}", True, (255, 255, 255)), (self.director.screen.get_rect().midleft[0] + 230, self.director.screen.get_rect().midleft[1] + 290))
        for btn in self.ability_buttons.values():
            btn.draw(self.director.screen)

