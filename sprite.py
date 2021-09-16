
from typing import Tuple

import pygame
from projection import Projection
from enum import Enum

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4



class Sprite:

    def __init__(self, name: str, pos: Tuple[int,int], facing: Tuple[int,int], img_set: list):
        self.name = name
        self.img_set = img_set
        self.pos = pos
        self.facing = facing
        self.allowed_facings = self.get_allowed_facings()
        self.amount_of_allowed_facings = len(self.allowed_facings)
    
    def move_a_square(self, tilemap_dimension = 13) -> bool:
        """Gets the new facing square after current facing square has been set to current position. facing[0] tells the """
        l = [self.facing[0], self.facing[1]]
        for i in (0,1):
            l[i] += self.facing[i] - self.pos[i]
        if l[0] < -1 or l[0] > 14 or l[1] < -1 or l[1] > 14:
            return False
        else:
            self.pos = self.facing
            self.facing = tuple(l)
            # Generate new allowed facings
            self.allowed_facings = self.get_allowed_facings()
            return True
    def set_facing(self, new_facing: Tuple[int, int]) -> bool:
        """Sets sprite facing if new sprite facing is cointained within list of allowed facings"""
        if new_facing in self.allowed_facings:
            self.facing = new_facing
            print("New facing acquired")
            return True
        return False
    
    def change_facing(self, direction: Direction):
        if direction == Direction.UP:
            self.facing = (self.pos[0], self.pos[1] - 1)
            print(f"FACING {direction}")
        elif direction == Direction.RIGHT:
            self.facing = (self.pos[0] + 1, self.pos[1])
            print(f"FACING {direction}")
        elif direction == Direction.DOWN:
            self.facing = (self.pos[0], self.pos[1] + 1)
            print(f"FACING {direction}")
        elif direction == Direction.LEFT:
            self.facing = (self.pos[0] - 1, self.pos[1])
            print(f"FACING {direction}")
    
    def set_pos(self, new_pos: Tuple[int, int]):
        l = [self.facing[0], self.facing[1]]
        for i in (0,1):
            l[i] = self.facing[i] - self.pos[i]
        self.pos = new_pos
        self.facing = (new_pos[0] + l[0], new_pos[1] + l[1])

        self.allowed_facings = self.get_allowed_facings()

    # def change_facing(self):
    #     print(self.allowed_facings.index(self.facing))
    #     print("vs.")
    #     print(self.amount_of_allowed_facings)
    #     index = self.allowed_facings.index(self.facing)
    #     index += 1
    #     if index >= self.amount_of_allowed_facings:
    #         self.facing = self.allowed_facings[0]
    #         index = 0
    #     else:
    #         self.facing = self.allowed_facings[index]
    
    def get_allowed_facings(self):
        return Projection.get_orthogonal_adjecant_squares(self.pos[0], self.pos[1], 14)

    def draw_sprite(self, display: pygame.Surface, img: int):
        display.blit(self.img_set[img], Projection.get_isometric_tile_center(self.pos[0], self.pos[1], 32, 16, (display.get_size()[0] / 2), (display.get_size()[1] / 2)))