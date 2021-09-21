from typing import Tuple
import pygame
import projection
from tile import Tile

class TileMap:
    def __init__(self, xw: int, yl: int, map: list[Tile]):
        self.xw = xw
        self.yl = yl
        self.map = map

    def get_tile_in_coor(self, x: int, y: int):
        """Returns the tile object at coordinates x, y"""
        for tile in self.map:
            if tile.xcoor == x and tile.ycoor == y:
                return tile
        return None
    
    def get_tiles_in_coords(self, coords: list[Tuple[int,int]]):
        """Returns the tile objects for given list with indices of tuples. Optimization idea: sort coords so that when tile found no need to start at the begining of tilmap"""
        tiles = []
        for coor in coords:
            for tile in self.map:
                if tile.xcoor == coor[0] and tile.ycoor == coor[1]:
                    tiles.append(tile)
        return tiles