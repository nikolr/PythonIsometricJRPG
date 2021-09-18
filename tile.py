from typing import Tuple
import pygame


class Tile:

    info_text_col = (255, 255, 255)

    width_and_height_multiplier = 10

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


    def get_tile_rect(self) -> pygame.Rect:

        #mouse_pos = pygame.mouse.get_pos()

        return pygame.Rect(self.__xcoor, self.__ycoor, 10, 10)

        

        # if tile_rect.collidepoint(mouse_pos):
        #     pass

        # text_img = font.render(str(self.get_tile_coor()), True, self.info_text_col)
        # text_len = text_img.get_width()

        #text_box = pygame.Surface((10, 10))

        #Draw tile and include info about the coordinates

        #Make the info appear on mouse hover

        #Implement for isometric tilemap

    # def text_objects(self):
    #     font = pygame.font.SysFont('Arial', 6)
    #     textsurface = font.render(self.__str__(), True, self.info_text_col)
    #     textrect = textsurface.get_rect()
    #     return textsurface, textrect

    # def get_text_surface(self) -> pygame.Surface:
    #     font = pygame.font.SysFont('Arial', 5)
    #     #print(pygame.font.get_fonts())
    #     return font.render(self.__str__(), True, self.info_text_col)

    # def add_text(self, rect: pygame.Rect, surface: pygame.Surface):
    #     self.game_screen.blit(rect, surface)

    def __str__(self):
        return f"{self.xcoor}, {self.ycoor}"