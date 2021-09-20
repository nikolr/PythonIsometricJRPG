from ability import Ability
import pygame

class Button:

    def __init__(self, color, x, y, width, height, ability: Ability):
        """Button should contain ability. Should draw range indicator when clicked. Should keep ability in memory after click.
            Check for viable targets with ability.get_possible_targets(). Afterwards play animation, deal damage, check for death and end game and get next state from state machine
        """
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.ability = ability

    def draw(self, screen, outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4), 0)
            
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.ability.name != '':
            font = pygame.font.Font("font/PressStart2P-vaV7.ttf", 10)
            text = font.render(self.ability.name, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
    def clicked(self, pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.isOver(pos):
            return True
        return False