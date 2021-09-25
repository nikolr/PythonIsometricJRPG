from data.scenes.title import Title
from pygame.constants import KEYDOWN
from data.config import SCREEN_SIZE_X, SCREEN_SIZE_Y
from pygame import mixer
import pygame
# from director import Director
from data.scenes.scene import Scene

class Win(Scene):
    def __init__(self, director) -> None:
        Scene.__init__(self, director)
        self.font = pygame.font.Font("resources/font/PressStart2P-vaV7.ttf", 20)
        self.director = director
        pygame.mixer.music.load('resources/sound/Prairie Oyster.wav')
        mixer.music.play(loops=-1)
    
    def on_update(self):
        pass

    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.director.change_scene(Title(self.director))
    
    def on_draw(self, screen):
        screen.fill((0, 0, 0))
        self.draw_text(screen, "You won", (255, 255, 255), SCREEN_SIZE_X/2, SCREEN_SIZE_Y/2)
        self.draw_text(screen, "Press enter to continue", (255, 255, 255), SCREEN_SIZE_X/2, SCREEN_SIZE_Y/1.5)

        
    
    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)