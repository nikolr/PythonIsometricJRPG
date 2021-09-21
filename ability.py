from pygame import display
import character
from enum import Enum
from tile import Tile
import projection
import ability
import pygame

class TargetingType(Enum):
    FACE = -1
    MOVE = 0
    SINGLE = 1
    ALL = 2
    AOE = 3
    LINE = 4


class Ability():

    def __init__(self, name: str, potency: int, ap_cost: int,range: int, targeting_type: TargetingType, user = None):
        self.name = name
        self.potency = potency
        self.ap_cost = ap_cost
        self.targeting_type = targeting_type
        self.range = range
        self.user = user

        self.zone_indicator = pygame.image.load("img/wbsprite.png").convert()
        self.zone_indicator.set_colorkey((0, 0, 0))
    
    def get_possible_targets(self, tiles: list[Tile]):
        """Gets an array of tiles, checks if characters occupy tiles and returns those characters"""
        targets = []
        for tile in tiles:
            if tile.occupier != None and tile.occupier_character.alive == True:
                targets.append(tile)
        return targets

    def get_tiles_in_range(self, tile: Tile):
        """Returns array of tiles within range amount of tiles. Diagonal tiles are distance 2 away. If range = 0 then return facing tile"""
        within_range = []
        within_range_storage = []

        if self.range > 0:
            within_range_storage.extend(projection.get_orthogonal_adjecant_squares(tile.xcoor, tile.ycoor))
        if self.range == 1:
            return within_range_storage
        for i in range(1, self.range):
            for tuple in within_range_storage:
                within_range.extend(projection.get_orthogonal_adjecant_squares(tuple[0], tuple[1]))
            within_range_storage.extend(within_range)
            within_range.clear()
        return list(set([i for i in within_range_storage]))

    def draw_range_indicator(self, disp: pygame.Surface, tile: Tile):
        """Draw selected abilities range"""
        if self.range == 0:
            user = tile.get_tile_occupier()
            facing_tile = user.facing_tile
            disp.blit(self.zone_indicator, projection.isometricprojection(facing_tile.xcoor, facing_tile.ycoor, 32, 16, (disp.get_size()[0] / 2), (disp.get_size()[1] / 2)))
            return True
        tiles_in_range = self.get_tiles_in_range(tile)
        for adj in tiles_in_range:
            disp.blit(self.zone_indicator, projection.isometricprojection(adj[0], adj[1], 32, 16, (disp.get_size()[0] / 2), (disp.get_size()[1] / 2)))
        return False

    def action(self, target_tile: Tile):
        pass


