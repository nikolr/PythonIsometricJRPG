from enum import Enum, auto
from data.tile import Tile
import data.projection as projection
import pygame

class TargetingType(Enum):
    FACE = auto()
    MOVE = auto()
    WAIT = auto()
    SINGLE = auto()
    ALL = auto()
    AOE = auto()
    LINE = auto()


class Ability():

    def __init__(self, name: str, potency: int, ap_cost: int,range: int, targeting_type: TargetingType, description = 'Figure it out yourself', user = None):
        self.name = name
        self.description = description
        self.potency = potency
        self.ap_cost = ap_cost
        self.targeting_type = targeting_type
        self.range = range
        self.user = user

        self.zone_indicator = pygame.image.load("resources/img/wbsprite.png").convert()
        self.zone_indicator.set_colorkey((0, 0, 0))
    
    def get_possible_targets(self, tiles: list[Tile]):
        """Gets an array of tiles, checks if characters occupy tiles and returns those characters"""
        targets = []
        for tile in tiles:
            if tile.occupier_character != None and tile.occupier_character.alive == True:
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
            within_range = []
            for tuple in within_range_storage:
                within_range.extend(projection.get_orthogonal_adjecant_squares(tuple[0], tuple[1]))
            within_range_storage.extend(within_range)
            
        return list(set([i for i in within_range_storage]))

    def draw_range_indicator(self, disp: pygame.Surface, tile: Tile):
        """Draw selected abilities range"""
        if self.range == 0:
            sprite = tile.get_tile_occupier()
            facing_tile = sprite.facing_tile
            disp.blit(self.zone_indicator, projection.isometricprojection(facing_tile.xcoor, facing_tile.ycoor, 32, 16, (disp.get_size()[0] / 2), (disp.get_size()[1] / 2)))
            return True
        if self.targeting_type == TargetingType.ALL:
            tiles_in_range = self.user.scene.map
            for row in tiles_in_range:
                for tile in row:
                    disp.blit(self.zone_indicator, projection.isometricprojection(tile.xcoor, tile.ycoor, 32, 16, (disp.get_size()[0] / 2), (disp.get_size()[1] / 2)))
            return True
        else:
            tiles_in_range = self.get_tiles_in_range(tile)
        for adj in tiles_in_range:
            disp.blit(self.zone_indicator, projection.isometricprojection(adj[0], adj[1], 32, 16, (disp.get_size()[0] / 2), (disp.get_size()[1] / 2)))
        return False

    def activate(self):
        target = self.user.scene.current_tile.occupier_character
        print(f"Targeted {self.user.scene.current_tile.occupier.name} with ability {self.name}")
        print(self.user.scene.current_character.action_points)
        self.user.scene.current_character.action_points = self.user.scene.current_character.action_points - self.ap_cost
        print(self.user.scene.current_character.action_points)
        target.take_damage(self.potency)
        if self.user.scene.current_character.action_points > 0:
            self.user.scene.state_machine.change_state(self.user.scene.turn_state)
        else:
            self.user.scene.upkeep()


