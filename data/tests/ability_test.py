from os import set_inheritable
from group_manager import GroupManager
from sprite import Sprite
from tilemap import TileMap
from tile import Tile
import projection
import unittest
from sprite import Sprite
from character import Character
from collections import deque
from attribute import Attribute
from attribute_modifier import AttributeModType, AttributeModifier
from stat_collection import StatCollection
from attribute_id import AttributeId
import ability
import pygame

class TestAbility(unittest.TestCase):
    def test_ability(self):
        #Ready sprites
        mage = pygame.image.load("img/mage1.png")
        mage.set_colorkey((0, 0, 0))
        wolf = pygame.image.load("img/wolf.png")
        wolf.set_colorkey((0, 0, 0))
        tr = pygame.image.load("img/wrsprite.png")
        tr.set_colorkey((0, 0, 0))
        f = open('map_full.txt')
        read_map = [[int(c) for c in row] for row in f.read().split('\n')]
        f.close()
        map = []
        for y, row in enumerate(read_map):
            for x, index in enumerate(row):
                map.append(Tile(x, y))
        tilemap = TileMap(13, 13, map)
        win = pygame.display.set_mode((0,0))
        swar = Sprite('warrior', (2, 5), (2, 4), tilemap, [])
        ahp = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        ams = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        ama = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        sca = StatCollection()
        sca.add_to_dict(AttributeId.HP, ahp)
        sca.add_to_dict(AttributeId.STRENGTH, ams)
        sca.add_to_dict(AttributeId.AGILITY, ama)
        cwar = Character('Warrior', sca, swar, counter = 14, innate_counter= 8)
        smage = Sprite('mage', (0, 0), (1, 0), tilemap, [])
        wmhp = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        wms = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        wma = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        sc = StatCollection()
        sc.add_to_dict(AttributeId.HP, wmhp)
        sc.add_to_dict(AttributeId.STRENGTH, wms)
        sc.add_to_dict(AttributeId.AGILITY, wma)
        cmage = Character('WhiteMage', sc, smage, counter = 15, innate_counter= 10)
        swolf = Sprite('wolf', (2, 3), (3, 3), tilemap, [])
        whp = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        ws = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        wa = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        scw = StatCollection()
        scw.add_to_dict(AttributeId.HP, whp)
        scw.add_to_dict(AttributeId.STRENGTH, ws)
        scw.add_to_dict(AttributeId.AGILITY, wa)
        cwolf = Character('Wolf', scw, swolf, counter = 21, innate_counter= 16)
        sshroom = Sprite('shroom', (4, 5), (5, 5), tilemap, [])
        shp = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        ss = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        sa = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        scs = StatCollection()
        scs.add_to_dict(AttributeId.HP, shp)
        scs.add_to_dict(AttributeId.STRENGTH, ss)
        scs.add_to_dict(AttributeId.AGILITY, sa)
        cshroom = Character('Shroom', scs, sshroom, counter = 22, innate_counter= 19)

        attack = ability.Ability("Slash", 5, 1, ability.TargetingType.SINGLE, 1, cwar)
        shoot = ability.Ability("Shoot", 3, 1, ability.TargetingType.SINGLE, 3, cwar)

        cwar.gain_ability(attack)
        cwar.gain_ability(shoot)

        cmage.gain_ability(attack)
        cmage.gain_ability(shoot)

        self.assertEqual(cwar.abilities[0].get_tiles_in_range(cwar.sprite.tile), projection.get_orthogonal_adjecant_squares(cwar.sprite.tile.xcoor, cwar.sprite.tile.ycoor))
        self.assertEqual(cwar.abilities[1].get_tiles_in_range(cwar.sprite.tile), [(3, 4), (3, 7), (4, 6), (0, 5), (2, 2), (1, 6), (2, 5), (1, 3), (2, 8), (4, 5), (3, 3), (3, 6), (2, 4), (0, 4), (2, 7), (1, 5), (3, 5), (4, 4), (5, 5), (1, 4), (0, 6), (2, 3), (1, 7), (2, 6)])
        self.assertEqual(cmage.abilities[0].get_tiles_in_range(cmage.sprite.tile), projection.get_orthogonal_adjecant_squares(cmage.sprite.tile.xcoor, cmage.sprite.tile.ycoor))
        self.assertEqual(cmage.abilities[1].get_tiles_in_range(cmage.sprite.tile),[(0, 1), (1, 2), (2, 1), (0, 0), (1, 1), (0, 3), (2, 0), (3, 0), (0, 2), (1, 0)])

if __name__ == '__main__':
    unittest.main()       
        