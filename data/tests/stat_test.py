from data.tile import Tile
import unittest

from data.attributes.attribute import Attribute
from data.attributes.attribute_id import AttributeId
from data.attributes.attribute_modifier import (AttributeModifier,
                                                AttributeModType)
from data.attributes.stat_collection import StatCollection
from data.character import Character
from data.sprite import DOWN, Sprite


class TestProjection(unittest.TestCase):
    def setUp(self):
        self.map = []
        for i in range(14):
            row = []
            for j in range(14):
                row.append(Tile(i, j))
            self.map.append(row)

        s1 = Sprite('mage', (4, 7), DOWN, map=self.map)
        wmhp = Attribute(AttributeId.HP, 100, 'Health',
                         'HP')
        wms = Attribute(AttributeId.STRENGTH, 5,
                        'Strength', 'STR')
        wma = Attribute(AttributeId.AGILITY, 10,
                        'Agility', 'AGI')
        sc = StatCollection()
        sc.add_to_dict(AttributeId.HP, wmhp)
        sc.add_to_dict(AttributeId.STRENGTH, wms)
        sc.add_to_dict(AttributeId.AGILITY, wma)
        self.t = Character('wm', sc, s1, counter=10)

    def test_attribute_debuff(self):
        fadb = AttributeModifier(
            AttributeModType.FLAT, AttributeId.AGILITY, -4, 1)
        self.t.stat_collection.get_attribute(
            AttributeId.AGILITY).add_modifier(fadb)
        self.assertEqual(self.t.stat_collection.get_attribute(
            AttributeId.AGILITY).value, 6, "Did not apply flat agility debuff correctly")

    def test_attribute_percent_buff(self):
        psb = AttributeModifier(
            AttributeModType.PERCENTMULTIPLY, AttributeId.STRENGTH, 0.5, 2)
        self.t.stat_collection.get_attribute(
            AttributeId.STRENGTH).add_modifier(psb)
        self.assertEqual(self.t.stat_collection.get_attribute(
            AttributeId.STRENGTH).value, 7.5, "Did not apply flat agility debuff correctly")

    def test_attribute_stack(self):
        psb = AttributeModifier(
            AttributeModType.PERCENTMULTIPLY, AttributeId.STRENGTH, 0.5, 2)
        self.t.stat_collection.get_attribute(
            AttributeId.STRENGTH).add_modifier(psb)
        fsb = AttributeModifier(AttributeModType.FLAT,
                                AttributeId.STRENGTH, 5, 1)
        self.t.stat_collection.get_attribute(
            AttributeId.STRENGTH).add_modifier(fsb)
        self.assertEqual(self.t.stat_collection.get_attribute(
            AttributeId.STRENGTH).value, 15, "Did not apply buffs in the correct order")

if __name__ == '__main__':
    unittest.main()
