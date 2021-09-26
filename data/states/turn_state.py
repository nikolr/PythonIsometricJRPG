import pygame
from data.states.state import State
from data.ui.button import Button
from data.ui import ui_module


class TurnState(State):
    """Keeps track of current character Action Points. After depletion or game end condition flags, get next state from queue? Or otherwise determine next state"""

    def __init__(self, director, scene) -> None:
        State.__init__(self, director)
        self.director = director
        self.scene = scene

        self.ability_buttons = {}
        self.utility_buttons = {}
        self.hovered_ability = None

        self.zone_indicator = pygame.image.load("resources/img/wbsprite.png").convert()
        self.zone_indicator.set_colorkey((0, 0, 0))

        self.ability_panel = pygame.Rect([director.screen.get_rect().midleft[0], director.screen.get_rect().midleft[1] + 280, 450, 200])
        self.name_panel = pygame.Rect([director.screen.get_rect().midleft[0], director.screen.get_rect().midleft[1] + 280, 225, 50])
        self.ap_panel = pygame.Rect([director.screen.get_rect().midleft[0] + 225, director.screen.get_rect().midleft[1] + 280, 225, 50])

        self.first_player_panel = pygame.Rect([director.screen.get_rect().midleft[0], director.screen.get_rect().midleft[1] - 150, 225, 125])
        self.second_player_panel = pygame.Rect([director.screen.get_rect().midleft[0], director.screen.get_rect().midleft[1]  - 25, 225, 125])
        self.third_player_panel = pygame.Rect([director.screen.get_rect().midleft[0], director.screen.get_rect().midleft[1] + 100, 225, 125])

        self.first_enemy_panel = pygame.Rect([director.screen.get_rect().topright[0] - 225, director.screen.get_rect().topright[1], 225, 125])
        self.second_enemy_panel = pygame.Rect([director.screen.get_rect().topright[0] - 225, director.screen.get_rect().topright[1] + 125, 225, 125])
        self.third_enemy_panel = pygame.Rect([director.screen.get_rect().topright[0] - 225, director.screen.get_rect().topright[1] + 250, 225, 125])
        self.fourth_enemy_panel = pygame.Rect([director.screen.get_rect().topright[0] - 225, director.screen.get_rect().topright[1] + 375, 225, 125])

        self.player_info_panel = pygame.Rect([director.screen.get_rect().midleft[0], director.screen.get_rect().midleft[1] - 150, 225, 375])
        self.enemy_info_panel = pygame.Rect([director.screen.get_rect().topright[0] - 225, director.screen.get_rect().topright[1], 225, 475])
        self.font = pygame.font.Font("resources/font/PressStart2P-vaV7.ttf", 25)

    def enter(self):
        print("Entered Turn State")
        self.ability_buttons.clear()
        for i in range(len(self.scene.current_character.abilities)):
            self.ability_buttons[f"{i}"] = Button((0,0,70), self.director.screen.get_rect().midleft[0], self.director.screen.get_rect().midleft[1] + 330 + (i * 30), 120, 35, self.scene.current_character.abilities[i])
        self.utility_buttons[1] = Button((0,0,70), self.director.screen.get_rect().midleft[0] + 120, self.director.screen.get_rect().midleft[1] + 330, 120, 35, self.scene.director.wait)
        
    def exit(self):
        print("Exited Turn State")
        pass
    def update(self):
        for btn in self.ability_buttons.values():
            if btn.isOver((self.scene.x_world, self.scene.y_world)):
                self.hovered_ability = btn.ability
        for btn in self.utility_buttons.values():
            if btn.isOver((self.scene.x_world, self.scene.y_world)):
                self.hovered_ability = btn.ability




    def render(self):
        pygame.draw.rect(self.director.screen,(100, 100, 100), self.ability_panel)

        pygame.draw.rect(self.director.screen,(100, 100, 100), self.player_info_panel)

        pygame.draw.rect(self.director.screen,(100, 100, 100), self.enemy_info_panel)

        pygame.draw.rect(self.director.screen,(0, 0, 0), self.first_player_panel, 3)
        pygame.draw.rect(self.director.screen,(0, 0, 0), self.second_player_panel, 3)
        pygame.draw.rect(self.director.screen,(0, 0, 0), self.third_player_panel, 3)

        pygame.draw.rect(self.director.screen,(0, 0, 0), self.first_enemy_panel, 3)
        pygame.draw.rect(self.director.screen,(0, 0, 0), self.second_enemy_panel, 3)
        pygame.draw.rect(self.director.screen,(0, 0, 0), self.third_enemy_panel, 3)
        pygame.draw.rect(self.director.screen,(0, 0, 0), self.fourth_enemy_panel, 3)

        pygame.draw.rect(self.director.screen,(0, 0, 0), self.name_panel, 3)
        pygame.draw.rect(self.director.screen,(0, 0, 0), self.ap_panel, 3)
        #Blit text into player info boxes
        ui_module.draw_character_info(self.director.screen, self.font, self.scene.group_manager.player_party, (255, 255, 255), self.director.screen.get_rect().midleft[0], self.director.screen.get_rect().midleft[1] - 130, 5, 120, 25)
        #Blit text into enemy info boxes
        ui_module.draw_character_info(self.director.screen,self.font, self.scene.group_manager.enemy_party, (255, 255, 255), self.director.screen.get_rect().topright[0], self.director.screen.get_rect().topright[1], -220, 125, 25)
        
        self.director.screen.blit(self.font.render(self.scene.current_character.name, True, (255, 255, 255)), (self.director.screen.get_rect().midleft[0], self.director.screen.get_rect().midleft[1] + 290))
        self.director.screen.blit(self.font.render(f"AP: {self.scene.current_character.action_points}", True, (255, 255, 255)), (self.director.screen.get_rect().midleft[0] + 230, self.director.screen.get_rect().midleft[1] + 290))
        for btn in self.ability_buttons.values():
            btn.draw(self.director.screen)
        for btn in self.utility_buttons.values():
            btn.draw(self.director.screen)

        

