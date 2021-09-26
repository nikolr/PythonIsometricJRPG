import unittest
from collections import deque
from context import data
import pygame
from data.attributes.attribute import Attribute
from data.attributes.attribute_id import AttributeId
from data.attributes.attribute_modifier import AttributeModifier, AttributeModType
from data.attributes.stat_collection import StatCollection
from data.character import Character
from data.group_manager import GroupManager
from data.sprite import Sprite
from data.tile import Tile
from data.tilemap import TileMap




class TestGroupManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        #Ready sprites
        mage = pygame.image.load("resources/img/mage1.png")
        mage.set_colorkey((0, 0, 0))
        wolf = pygame.image.load("resources/img/wolf.png")
        wolf.set_colorkey((0, 0, 0))
        tr = pygame.image.load("resources/img/wrsprite.png")
        tr.set_colorkey((0, 0, 0))
        f = open('resources/map_full.txt')
        read_map = [[int(c) for c in row] for row in f.read().split('\n')]
        f.close()
        tmap = [] 
        for y, row in enumerate(read_map):
            for x, index in enumerate(row):
                tmap.append(Tile(x, y))
        
        
        ahp = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        ams = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        ama = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        cls.sca = StatCollection()
        cls.sca.add_to_dict(AttributeId.HP, ahp)
        cls.sca.add_to_dict(AttributeId.STRENGTH, ams)
        cls.sca.add_to_dict(AttributeId.AGILITY, ama)

        
        wmhp = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        wms = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        wma = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        cls.sc = StatCollection()
        cls.sc.add_to_dict(AttributeId.HP, wmhp)
        cls.sc.add_to_dict(AttributeId.STRENGTH, wms)
        cls.sc.add_to_dict(AttributeId.AGILITY, wma)

        
        whp = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        ws = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        wa = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        cls.scw = StatCollection()
        cls.scw.add_to_dict(AttributeId.HP, whp)
        cls.scw.add_to_dict(AttributeId.STRENGTH, ws)
        cls.scw.add_to_dict(AttributeId.AGILITY, wa)
        
        shp = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        ss = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        sa = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        cls.scs = StatCollection()
        cls.scs.add_to_dict(AttributeId.HP, shp)
        cls.scs.add_to_dict(AttributeId.STRENGTH, ss)
        cls.scs.add_to_dict(AttributeId.AGILITY, sa)
        cls.tilemap = TileMap(13, 13, tmap)
        cls.swar = Sprite('warrior', (2, 5), (2, 4), cls.tilemap, [])
        cls.smage = Sprite('mage', (4, 7), (4, 6), cls.tilemap, [])
        cls.swolf = Sprite('wolf', (2, 3), (3, 3),cls.tilemap, [])
        cls.sshroom = Sprite('shroom', (4, 5), (5, 5), cls.tilemap, [])
        cls.cwar = Character('Warrior', cls.sca, cls.swar, counter = 14, innate_counter= 8)
        cls.cmage = Character('WhiteMage', cls.sc, cls.smage, counter = 15, innate_counter= 10)
        cls.cwolf = Character('Wolf', cls.scw, cls.swolf, counter = 21, innate_counter= 16)
        cls.cshroom = Character('Shroom', cls.scs, cls.sshroom, counter = 22, innate_counter= 19)
        cls.gm = GroupManager([cls.cmage, cls.cwolf, cls.cwar, cls.cshroom])

    def test_group_manager(self):
        self.gm.determine_turn_queue()
        self.assertEqual(self.gm.get_list(), ['Warrior', 'WhiteMage', 'Wolf', 'Warrior', 'Shroom', 'WhiteMage', 'Warrior', 'WhiteMage', 'Wolf', 'Warrior'], "Created queue differed from expected")
        
        
if __name__ == '__main__':
    unittest.main()       
        
        
