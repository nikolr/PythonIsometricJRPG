import pygame
import projection
from tile import Tile

class TileMap:
    def __init__(self, xw: int, yl: int, map_data : str):
        self.xw = xw
        self.yl = yl
        self.map_data = map_data
    
    def get_map_data(self) :
        f = open(self.map_data)
        map = [[int(c) for c in row] for row in f.read().split('\n')]
        f.close()
        return map
    
    #Test function. Create a flat x*y grid of tiles.
    def make_full_map(self) -> list:
        fullmap = []
        isometricmap = []
        for y, row in enumerate(self.get_map_data()):
            for x, index in enumerate(row):
                fullmap.append(Tile(x, y))
                xi, yi = projection.isometricprojection(x, y, 32, 16, 0, 0)
                isometricmap.append(Tile(xi, yi))

        return fullmap, isometricmap

