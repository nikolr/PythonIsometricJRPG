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
        self.font = pygame.font.Font("font/PressStart2P-vaV7.ttf", 25)

    def enter(self):
        print("Entered Turn State")
        self.ability_buttons.clear()
        for i in range(len(self.scene.current_character.abilities)):
            # self.ability_buttons.append(Button((0,0,70), self.director.screen.get_rect().midleft[0], self.director.screen.get_rect().midleft[1] + 300 + (i + 20), 100, 50, ab))
            # self.ability_buttons[f"{i}"] = self.scene.current_character.abilities[i]
            self.ability_buttons[f"{i}"] = Button((0,0,70), self.director.screen.get_rect().midleft[0], self.director.screen.get_rect().midleft[1] + 330 + (i * 30), 100, 35, self.scene.current_character.abilities[i])
    def exit(self):
        #Close character action panel
        pass
    def update(self):
        for btn in self.ability_buttons.values():
            if btn.isOver((self.scene.x_world, self.scene.y_world)):
                self.hovered_ability = btn.ability



    def render(self):
        pygame.draw.rect(self.director.screen,(100, 100, 100), self.ability_panel)
        pygame.draw.rect(self.director.screen,(0, 0, 0), self.name_panel, 3)
        self.director.screen.blit(self.font.render(self.scene.current_character.name, True, (255, 255, 255)), (self.director.screen.get_rect().midleft[0], self.director.screen.get_rect().midleft[1] + 290))
        for btn in self.ability_buttons.values():
            btn.draw(self.director.screen)

