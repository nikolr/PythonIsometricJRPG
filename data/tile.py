from typing import Tuple
# from sprite import Sprite
import pygame

#Make the info appear on mouse hover

class Tile:

    def __init__(self, xcoor: int, ycoor: int, game_screen = None, tile_image = None):
        pygame.init()
        
        self.__xcoor = xcoor
        self.__ycoor = ycoor
        self.occupied = False
        self.occupier = None
        self.occupier_character = None
        self.game_screen = game_screen
        self.tile_image = tile_image
        
    @property
    def xcoor(self) -> int:
        return self.__xcoor
    @xcoor.setter
    def xcoor(self, x: int):
        self.__xcoor = x
    @property
    def ycoor(self) -> int:
        return self.__ycoor
    @ycoor.setter
    def ycoor(self, y: int):
        self.__ycoor = y
    
    def set_tile_img(self, img):
        self.tile_image = img

    def get_tile_coor(self) -> Tuple[int,int]:
        return (self.__xcoor, self.__ycoor)
    
    def set_tile_coor(self, x: int, y: int):
        self.__xcoor = x
        self.__ycoor = y

    # def is_over(self, pos):
    #     #Pos is the mouse position or a tuple of (x,y) coordinates
    #     if pos[0] > self.x and pos[0] < self.x + self.width:
    #         if pos[1] > self.y and pos[1] < self.y + self.height:
    #             return True
    #     return False

    # def clicked(self, pos, event):
    #     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_over(pos):
    #         return True
    #     return False

    def get_tile_occupier(self):
        return self.occupier

    def get_tile_occupier_character(self):
        return self.occupier_character

    def __str__(self):
        return f"{self.xcoor}, {self.ycoor}"