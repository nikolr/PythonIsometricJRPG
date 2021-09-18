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