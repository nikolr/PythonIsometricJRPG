from ability import Ability
from enum import IntEnum
from typing import Tuple

import pygame

import projection
from tilemap import TileMap


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3



class Sprite:

    def __init__(self, name: str, pos: Tuple[int,int], facing: Tuple[int,int], map: TileMap, img_set: list, character = None):
        self.name = name
        self.character = character
        self.img_set = img_set
        self.pos = pos
        self.facing = facing
        self.map = map
        self.tile = map.get_tile_in_coor(pos[0], pos[1])
        self.tile.occupied = True
        self.tile.occupier = self
        self.facing_tile = map.get_tile_in_coor(facing[0], facing[1])
        self.offset = self.get_direction()
        self.allowed_facings = self.get_allowed_facings()
        self.amount_of_allowed_facings = len(self.allowed_facings)
    
    def move_a_square(self, tilemap_dimension = 13) -> bool:
        """Gets the new facing square after current facing square has been set to current position. facing[0] tells the """
        l = [self.facing[0], self.facing[1]]
        for i in (0,1):
            l[i] += self.facing[i] - self.pos[i]
        if l[0] < -1 or l[0] > 14 or l[1] < -1 or l[1] > 14:
            return False
        elif self.facing_tile.occupied == True:
            print(f"Cannot move onto tile. There is a {self.facing_tile.occupier} on it")
            return False
        else:
            self.tile.occupied = False
            self.pos = self.facing
            self.tile = self.map.get_tile_in_coor(self.pos[0], self.pos[1])
            self.tile.occupier = self
            self.tile.occupied = True
            self.facing = tuple(l)
            if self.map.get_tile_in_coor(self.facing[0], self.facing[1]) == None:
                return False
            self.facing_tile = self.map.get_tile_in_coor(self.facing[0], self.facing[1])
            # Generate new allowed facings
            self.allowed_facings = self.get_allowed_facings()
            return True
    def set_facing(self, new_facing: Tuple[int, int]) -> bool:
        """Sets sprite facing if new sprite facing is cointained within list of allowed facings"""
        if new_facing in self.allowed_facings:
            self.facing = new_facing
            self.facing_tile = self.map.get_tile_in_coor(self.facing[0], self.facing[1])
            print("New facing acquired")
            return True
        return False
    
    def change_facing(self, direction: Direction):
        if direction == Direction.UP:
            self.facing = (self.pos[0], self.pos[1] - 1)
            self.facing_tile = self.map.get_tile_in_coor(self.facing[0], self.facing[1])
            # print(f"FACING {direction}")
        elif direction == Direction.RIGHT:
            self.facing = (self.pos[0] + 1, self.pos[1])
            self.facing_tile = self.map.get_tile_in_coor(self.facing[0], self.facing[1])
            # print(f"FACING {direction}")
        elif direction == Direction.DOWN:
            self.facing = (self.pos[0], self.pos[1] + 1)
            self.facing_tile = self.map.get_tile_in_coor(self.facing[0], self.facing[1])
            # print(f"FACING {direction}")
        elif direction == Direction.LEFT:
            self.facing = (self.pos[0] - 1, self.pos[1])
            self.facing_tile = self.map.get_tile_in_coor(self.facing[0], self.facing[1])
            # print(f"FACING {direction}")
    
    def set_pos(self, new_pos: Tuple[int, int]):
        l = [self.facing[0], self.facing[1]]
        for i in (0,1):
            l[i] = self.facing[i] - self.pos[i]
        self.pos = new_pos
        self.facing = (new_pos[0] + l[0], new_pos[1] + l[1])

        self.allowed_facings = self.get_allowed_facings()
    
    def get_allowed_facings(self):
        return projection.get_orthogonal_adjecant_squares(self.pos[0], self.pos[1], 14)

    def get_direction(self):
        off = (self.pos[0] - self.facing[0], self.pos[1] - self.facing[1])
        if off == (0,-1):
            return int(Direction.UP)
        if off == (1,0):
            return int(Direction.RIGHT)    
        if off == (0,1):
            return int(Direction.DOWN)
        if off == (-1,0):
            return int(Direction.LEFT)

    def draw_sprite(self, display: pygame.Surface):
        # display.blit(self.img_set[self.get_direction()], projection.get_isometric_tile_center(self.pos[0], self.pos[1], 32, 16, (display.get_size()[0] / 2), (display.get_size()[1] / 2)))
        display.blit(self.img_set[0], projection.get_isometric_tile_center(self.pos[0], self.pos[1], 32, 16, (display.get_size()[0] / 2), (display.get_size()[1] / 2)))


