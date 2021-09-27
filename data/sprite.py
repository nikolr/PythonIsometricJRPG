from typing import Tuple

import pygame

import data.projection as projection
from data.tilemap import TileMap
from collections import namedtuple

direction = namedtuple('up', 'x y')
UP = direction(0, 1)
RIGHT = direction(-1, 0)
DOWN = direction(0, -1)
LEFT = direction(1, 0)

#If attacking sprite has sprite.facing_direction = UP and target sprite has sprite has sprite.facing_direction = UP, then (0,1)+(0,1) = (0,2) => backstab
#If attacking sprite has sprite.facing_direction = UP and target sprite has sprite has sprite.facing_direction = DOWN, then (0,1)+(0,-1) = (0,0) => frontal attack
#So if the absolute value of the addition for x or y is 2 => backstab, if it is 0 the front
#Maybe check the additions absolute values and raise backstab flag as needed


#TODO Make simple sprite sheets and implement animations with them
#On damaged => wobble in all directions
#On ability use => Take a step towards facing tile

class Sprite:

    def __init__(self, name: str, pos: Tuple[int,int], facing_direction: direction, map = [[]], img_set: list = [], character = None):
        self.name = name
        self.character = character
        self.img_set = img_set
        self.pos = pos
        self.facing_direction = facing_direction
        self.facing = projection.add_tuples(pos, facing_direction)
        self.map = map
        self.tile = map[self.pos[0]][self.pos[1]]
        self.tile.occupied = True
        self.tile.occupier = self
        self.facing_tile = map[self.facing[0]][self.facing[1]]
        self.allowed_facings = self.get_allowed_facings()
        self.amount_of_allowed_facings = len(self.allowed_facings)

        self.zone_of_control = []
        # self.zone_of_control = map.get_tiles_in_coords(projection.get_adjecant_squares(self.tile.xcoor, self.tile.ycoor))
        # for (x,y) in projection.get_adjecant_squares(self.tile.xcoor, self.tile.ycoor):
        #     print(map[x][y])
        #     self.zone_of_control.append(map[x][y])
        # print(self.zone_of_control)
        
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
        elif self.facing_tile.xcoor <= 0 or self.facing_tile.ycoor <= 0 or self.facing_tile.xcoor >= 13 or self.facing_tile.ycoor >= 13:
            print(f"Cannot move out of bounds")
            return False
        else:
            self.tile.occupier = None
            self.tile.occupier_character = None
            self.tile.occupied = False
            self.pos = self.facing
            self.tile = self.map[self.pos[0]][self.pos[1]]
            self.tile.occupier = self
            self.tile.occupied = True
            self.facing = tuple(l)
            if self.map[self.facing[0]][self.facing[1]] == None:
                return False
            self.facing_tile = self.map[self.facing[0]][self.facing[1]]
            # Generate new allowed facings
            self.allowed_facings = self.get_allowed_facings()
            return True

    # def move_x(self, max_ap : int, tilemap_dimension = 13):
    #     """"""

    def move_backwards(self, tilemap_dimension = 13) -> bool:
        """Move a square backwards while maintaining facing direction"""
        new_pos = projection.sub_tuples(self.pos, self.facing_direction)
        print(new_pos)
        if new_pos[0] < 0 or new_pos[0] >= tilemap_dimension or new_pos[1] < 0 or new_pos[1] >= tilemap_dimension:
            print("FLASE!?!?!?")
            return False
        else:
            #Update starting tile status to unoccupied
            self.tile.occupier = None
            self.tile.occupier_character = None
            self.tile.occupied = False

            self.facing = self.pos
            self.facing_tile = self.map[self.facing[0]][self.facing[1]]
            self.pos = new_pos

            #Update tile status
            self.tile = self.map[self.pos[0]][self.pos[1]]
            self.tile.occupier = self
            self.tile.occupied = True
            self.allowed_facings = self.get_allowed_facings()
            return True
    def set_facing(self, new_facing: Tuple[int, int]) -> bool:
        """Sets sprite facing if new sprite facing is cointained within list of allowed facings"""
        if new_facing in self.allowed_facings:
            self.facing = new_facing
            self.facing_direction = projection.sub_tuples(self.facing, self.pos)
            self.facing_tile = self.map[self.facing[0]][self.facing[1]]
            print("New facing acquired")
            return True
        return False

    def change_facing(self, direction: direction):
        """takes direction as an argument and sets facing to the tile in that direction"""
        new_facing = projection.add_tuples(self.pos, direction)
        self.set_facing(new_facing)
    
    def set_pos(self, new_pos: Tuple[int, int]):
        l = [self.facing[0], self.facing[1]]
        for i in (0,1):
            l[i] = self.facing[i] - self.pos[i]
        self.pos = new_pos
        self.facing = (new_pos[0] + l[0], new_pos[1] + l[1])

        self.allowed_facings = self.get_allowed_facings()
    
    def get_allowed_facings(self):
        return projection.get_orthogonal_adjecant_squares(self.pos[0], self.pos[1])

    def draw_sprite(self, display: pygame.Surface):
        # display.blit(self.img_set[self.get_direction()], projection.get_isometric_tile_center(self.pos[0], self.pos[1], 32, 16, (display.get_size()[0] / 2), (display.get_size()[1] / 2)))
        display.blit(self.img_set[0], projection.get_isometric_tile_center(self.pos[0], self.pos[1], 32, 16, (display.get_size()[0] / 2), (display.get_size()[1] / 2)))


