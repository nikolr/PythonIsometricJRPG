from data.tile import Tile
import data.projection as projection
import pygame
from data.abilities.ability import Ability

class Bash(Ability):
    def __init__(self, name: str, potency: int, ap_cost: int, range: int, targeting_type, user):
        super().__init__(name, potency, ap_cost, range, targeting_type, user=user)
        self.description = "Weak smack with a staff"
    def get_tiles_in_range(self, tile: Tile):
        """Returns array of tiles within range amount of tiles. Diagonal tiles are distance 2 away. If range = 0 then return facing tile"""
        return [(self.user.sprite.facing_tile.xcoor, self.user.sprite.facing_tile.ycoor)]

    def draw_range_indicator(self, disp: pygame.Surface, tile: Tile):
        """Draw selected abilities range"""
        disp.blit(self.zone_indicator, projection.isometricprojection(self.user.sprite.facing_tile.xcoor, self.user.sprite.facing_tile.ycoor, 32, 16, (disp.get_size()[0] / 2), (disp.get_size()[1] / 2)))
