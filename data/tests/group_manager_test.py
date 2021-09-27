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
        cls.map = []
        for i in range(14):
            row = []
            for j in range(14):
                row.append(Tile(i, j))
            cls.map.append(row)
        
        
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
        cls.swar = Sprite('warrior', (2, 5), (2, 4), cls.map, [])
        cls.smage = Sprite('mage', (4, 7), (4, 6), cls.map, [])
        cls.swolf = Sprite('wolf', (2, 3), (3, 3),cls.map, [])
        cls.sshroom = Sprite('shroom', (4, 5), (5, 5), cls.map, [])
        cls.cwar = Character('Warrior', cls.sca, cls.swar, counter = 1, innate_counter= 10)
        cls.cmage = Character('WhiteMage', cls.sc, cls.smage, counter = 2, innate_counter= 10)
        cls.cwolf = Character('Wolf', cls.scw, cls.swolf, counter = 3, innate_counter= 10)
        cls.cshroom = Character('Shroom', cls.scs, cls.sshroom, counter = 4, innate_counter= 10)
        cls.gm = GroupManager([cls.cmage, cls.cwolf, cls.cwar, cls.cshroom])

    def test_group_manager(self):
        self.gm.determine_turn_queue()
        self.assertEqual(self.gm.get_list(), ['Warrior', 'WhiteMage', 'Wolf', 'Shroom', 'Warrior', 'WhiteMage', 'Wolf', 'Shroom', 'Warrior', 'WhiteMage'], "Created queue differed from expected")
if __name__ == '__main__':
    unittest.main()       
        
        
