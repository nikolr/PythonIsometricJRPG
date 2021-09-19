from config import SCREEN_SIZE_X, SCREEN_SIZE_Y
# import pygame_gui
class Scene:
     """Represents a scene of the game.
 
     Scenes must be created inheriting this class attributes
     in order to be used afterwards as menus, introduction screens,
     etc."""
 
     def __init__(self, director):
        self.director = director
        self.state_stack = []
      #   self.manager = pygame_gui.UIManager((SCREEN_SIZE_X, SCREEN_SIZE_Y))
 
     def on_update(self):
        "Called from the director and defined on the subclass."
 
        raise NotImplementedError("on_update abstract method must be defined in subclass.")
 
     def on_event(self, event):
        "Called when a specific event is detected in the loop."
 
        raise NotImplementedError("on_event abstract method must be defined in subclass.")
 
     def on_draw(self, screen):
        "Called when something needs to be drawn within the scene"
 
        raise NotImplementedError("on_draw abstract method must be defined in subclass.")
