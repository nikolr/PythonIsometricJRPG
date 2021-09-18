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


    def get_tile_occupier(self):
        return self.occupier

    def __str__(self):
        return f"{self.xcoor}, {self.ycoor}"