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
import pygame

class TestProjection(unittest.TestCase):
    def test_sprite(self):
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
        swar = Sprite('warrior', (2, 5), (2, 4), tilemap, [])
        ahp = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        ams = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        ama = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        sca = StatCollection()
        sca.add_to_dict(AttributeId.HP, ahp)
        sca.add_to_dict(AttributeId.STRENGTH, ams)
        sca.add_to_dict(AttributeId.AGILITY, ama)
        cwar = Character('Warrior', sca, swar, counter = 14, innate_counter= 8)
        smage = Sprite('mage', (4, 7), (4, 6), tilemap, [])
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
        gm = GroupManager([cmage, cwolf, cwar, cshroom])
        gm.determine_turn_queue()
        gm.print_queue()
if __name__ == '__main__':
    unittest.main()       
        
        
