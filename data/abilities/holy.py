from data.tile import Tile
from data.abilities.ability import Ability

class Holy(Ability):
    def __init__(self, name: str, potency: int, ap_cost: int, range: int, targeting_type, user):
        super().__init__(name, potency, ap_cost, range, targeting_type, user=user)
        self.description = "Kill everyone"

    def activate(self):
        """Get target characters in get_possible_targets and deal flat damage on all"""
        targets = self.get_possible_targets(self.get_aoe())
        for target in targets:
            print(target.occupier_character.name)
        self.user.action_points = self.user.action_points - self.ap_cost
        for t in targets:
            t.occupier_character.take_damage(self.potency)
            print(f"{t.occupier_character.name} took {self.potency} damage")
        if self.user.action_points > 0:
            self.user.scene.state_machine.change_state(self.user.scene.turn_state)
        else:
            self.user.scene.upkeep()
    def get_tiles_in_range(self, tile: Tile):
        """Returns array of tiles within range amount of tiles. Diagonal tiles are distance 2 away. If range = 0 then return facing tile"""
        return self.user.scene.tilemap.map

    def get_aoe(self):
        """Returns array of tiles within range amount of tiles. Diagonal tiles are distance 2 away. If range = 0 then return facing tile"""
        return self.user.scene.tilemap.map

    # def draw_range_indicator(self, disp: pygame.Surface, tile: Tile):
    #     """Draw selected abilities range"""
    #     tiles_in_range = self.get_tiles_in_range(tile)
    #     for adj in tiles_in_range:
    #         disp.blit(self.zone_indicator, projection.isometricprojection(adj[0], adj[1], 32, 16, (disp.get_size()[0] / 2), (disp.get_size()[1] / 2)))