from data.abilities.ability import Ability, TargetingType
import unittest

import data.projection as projection
import pygame
from data.character import Character
from data.attributes.attribute import Attribute
from data.attributes.attribute_id import AttributeId
from data.attributes.stat_collection import StatCollection
from data.sprite import Sprite
from data.tile import Tile


class TestAbility(unittest.TestCase):

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
        pygame.display.set_mode((0,0))
        swar = Sprite('warrior', (2, 5), (2, 4), cls.map, [])
        ahp = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        ams = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        ama = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        sca = StatCollection()
        sca.add_to_dict(AttributeId.HP, ahp)
        sca.add_to_dict(AttributeId.STRENGTH, ams)
        sca.add_to_dict(AttributeId.AGILITY, ama)
        cls.cwar = Character('Warrior', sca, swar, counter = 14, innate_counter= 8)
        smage = Sprite('mage', (0, 0), (1, 0), cls.map, [])
        wmhp = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        wms = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        wma = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        sc = StatCollection()
        sc.add_to_dict(AttributeId.HP, wmhp)
        sc.add_to_dict(AttributeId.STRENGTH, wms)
        sc.add_to_dict(AttributeId.AGILITY, wma)
        cls.cmage = Character('WhiteMage', sc, smage, counter = 15, innate_counter= 10)

        attack = Ability("Slash", 20, 5, 1, TargetingType.SINGLE, cls.cwar)
        shoot = Ability("Shoot",20, 2, 3, TargetingType.SINGLE, cls.cwar)

        cls.cwar.gain_ability(attack)
        cls.cwar.gain_ability(shoot)

        cls.cmage.gain_ability(attack)
        cls.cmage.gain_ability(shoot)

    def test_ability(self):

        self.assertEqual(self.cwar.abilities[0].get_tiles_in_range(self.cwar.sprite.tile), projection.get_orthogonal_adjecant_squares(self.cwar.sprite.tile.xcoor, self.cwar.sprite.tile.ycoor))
        self.assertEqual(self.cwar.abilities[1].get_tiles_in_range(self.cwar.sprite.tile), [(3, 4), (3, 7), (4, 6), (0, 5), (2, 2), (1, 6), (2, 5), (1, 3), (2, 8), (4, 5), (3, 3), (3, 6), (2, 4), (0, 4), (2, 7), (1, 5), (3, 5), (4, 4), (5, 5), (1, 4), (0, 6), (2, 3), (1, 7), (2, 6)])

        self.assertEqual(self.cmage.abilities[0].get_tiles_in_range(self.cmage.sprite.tile), projection.get_orthogonal_adjecant_squares(self.cmage.sprite.tile.xcoor, self.cmage.sprite.tile.ycoor))
        self.assertEqual(self.cmage.abilities[1].get_tiles_in_range(self.cmage.sprite.tile),[(0, 1), (1, 2), (2, 1), (0, 0), (1, 1), (0, 3), (2, 0), (3, 0), (0, 2), (1, 0)])

if __name__ == '__main__':
    unittest.main()       
        