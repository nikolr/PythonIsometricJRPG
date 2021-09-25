import data.scenes.title
from pygame.constants import KEYDOWN
from data.config import SCREEN_SIZE_X, SCREEN_SIZE_Y
from pygame import mixer
import pygame
from data.scenes.scene import Scene

class Defeat(Scene):
    def __init__(self, director) -> None:
        Scene.__init__(self, director)
        self.font = pygame.font.Font("font/PressStart2P-vaV7.ttf", 20)
        self.director = director
        pygame.mixer.music.load('Prairie Oyster.wav')
        mixer.music.play(loops=-1)
    
    def on_update(self):
        pass

    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.director.change_scene(data.scenes.title.Title(self.director))
    
    def on_draw(self, screen):
        screen.fill((0, 0, 0))
        self.draw_text(screen, "Your party has been vanquished", (255, 255, 255), SCREEN_SIZE_X/2, SCREEN_SIZE_Y/2)
        self.draw_text(screen, "Press enter to continue", (255, 255, 255), SCREEN_SIZE_X/2, SCREEN_SIZE_Y/1.5)

        
    
    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)