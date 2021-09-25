from director import Director
import pygame
from state import State

class PauseMenu(State):
    def __init__(self, director: Director) -> None:
        super().__init__()

    def render(self, screen):
        pass