
import win, defeat
from os import close
from stat_collection import StatCollection
from character import Character
import projection

class Wolf(Character):
    def __init__(self, name: str, stat_collection: StatCollection, sprite, playable: bool = False, scene=None, base_action_points=4, counter=10, innate_counter=10):
        super().__init__(name, stat_collection, sprite, playable=playable, scene=scene, base_action_points=base_action_points, counter=counter, innate_counter=innate_counter)
    
        self.abilities = []

    def gain_ability(self, ability):
        return super().gain_ability(ability)

    def act(self):
        #Find closest playable character
        closest = projection.get_closest(self.sprite.pos, self.scene.group_manager.player_sprites)

        print(closest)
        #Get tile from point and get character from tile
        tile = self.scene.tilemap.get_tile_in_coor(closest[0], closest[1])
        print(tile)
        target = tile.get_tile_occupier_character()
        print(target)
        if target is None:
            return False
        #If already in position, attack
        if self.sprite.facing == (tile.xcoor, tile.ycoor):
            print("Right in front, commencing attack")
            # Of course we want ability(target). For now we do this
            target.take_damage(self.abilities[2].potency)
            #Reduce ap
            self.action_points = self.action_points - self.abilities[2].ap_cost
            if self.scene.group_manager.dead_character_indicator == True:

                print("Removing dead characters at the end of turn")
                self.scene.group_manager.remove_dead_characters()
                if self.scene.group_manager.player_party_is_empty() == True:
                    print("The party is literally empty")
                    self.scene.director.change_scene(win.Win(self.director))
                elif self.scene.group_manager.enemy_party_is_empty() == True:
                    """Call win state or lose state"""
                    self.scene.director.change_scene(defeat.Defeat(self.director))
            return True
        #If already next to target, change facing
        elif target.sprite.pos in projection.get_orthogonal_adjecant_squares(self.sprite.pos[0], self.sprite.pos[1]):
            print("Need to turn before I can attack")
            print(self.sprite.facing)
            self.sprite.set_facing(target.sprite.pos)
            print(self.sprite.facing)
            self.action_points = self.action_points - self.abilities[1].ap_cost
            return True
        #If on the same row or column and facing towards target, move
        elif target.sprite.pos[0] == self.sprite.pos[0] and target.sprite.pos in projection.get_line(self.sprite.pos, self.sprite.facing):
            print("Same row, move forward")
            self.sprite.move_a_square()
            self.action_points = self.action_points - self.abilities[0].ap_cost
            return True
        elif target.sprite.pos[1] == self.sprite.pos[1] and target.sprite.pos in projection.get_line(self.sprite.pos, self.sprite.facing):
            print("Same column, move forward")
            self.sprite.move_a_square()
            self.action_points = self.action_points - self.abilities[0].ap_cost
            return True
        #If not on the same axis but facing where the axis is, move towards axis
        #Move to same row/column if possible
        # elif 
        #Change facing so that can align with target with the least moves possible
        #Move so that facing_tile == targets tile
        #Attack as many times as possible
        #Wait with rest of ap
        else: 
            print("Fuck it, can't think of anything")
            self.sprite.move_a_square()
            self.action_points = self.action_points - self.abilities[0].ap_cost
            return False
        