# Modules
import pygame_gui
from config import SCREEN_SIZE_X, SCREEN_SIZE_Y
import pygame, sys
 
class Director:
    """Represents the main object of the game.
 
    The Director object keeps the game on, and takes care of updating it,
    drawing it and propagate events.
 
    This object must be used with Scene objects that are defined later."""
 
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))
        print("pygame.display initialized!")
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Tile based board demo")
        self.scene = None
        self.quit_flag = False
        self.clock = pygame.time.Clock()
        self.time_delta = None
        
        #UImanager
        # self.manager = pygame_gui.UIManager((SCREEN_SIZE_X, SCREEN_SIZE_Y))

        
 
    def loop(self):
        "Main game loop."
 
        while not self.quit_flag:
            # self.time_delta = self.clock.tick(60)/1000.0
            self.time_delta = self.clock.tick(60)
 
            # Exit events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
 
                # Detect events
                self.scene.on_event(event)
                # self.scene.manager.process_events(event)
 
            # Update scene
            
            self.scene.on_update()
            # self.scene.manager.update(self.time_delta)
 
            # Draw the screen
            
            self.scene.on_draw(self.screen)
            # self.scene.manager.draw_ui(self.screen)
            pygame.display.flip()
 
    def change_scene(self, scene):
        "Changes the current scene."
        self.scene = scene
 
    def quit(self):
        self.quit_flag = True