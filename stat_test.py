from attribute_modifier import AttributeModType, AttributeModifier
from stat_collection import StatCollection
from attribute_id import AttributeId
import unittest
from sprite import Sprite
from attribute import Attribute
from character import Character
#Movement from (0,0) to (1,0) should increase world coordinates by tilewidth/2 in x and tileheight/2 in y

class TestProjection(unittest.TestCase):
    def test_attribute(self):
        s1 = Sprite('mage', (4,7), (4,6), [])
        wmhp = Attribute(AttributeId.HP, 100, 'Health', 'Hit points until down')
        wms = Attribute(AttributeId.STRENGTH, 5, 'Health', 'Hit points until down')
        wma = Attribute(AttributeId.AGILITY, 10, 'Health', 'Hit points until down')
        sc = StatCollection()
        sc.add_to_dict(AttributeId.HP, wmhp)
        sc.add_to_dict(AttributeId.STRENGTH, wms)
        sc.add_to_dict(AttributeId.AGILITY, wma)
        t = Character('wm', sc, s1, counter = 10)
  
        fadb = AttributeModifier(AttributeModType.FLAT, AttributeId.AGILITY, -4, 1)
        t.stat_collection.get_attribute(AttributeId.AGILITY).add_modifier(fadb)
        self.assertEqual(t.stat_collection.get_attribute(AttributeId.AGILITY).value, 6, "Did not apply flat agility debuff correctly")

        psb = AttributeModifier(AttributeModType.PERCENTMULTIPLY, AttributeId.STRENGTH, 0.5, 2)
        t.stat_collection.get_attribute(AttributeId.STRENGTH).add_modifier(psb)
        self.assertEqual(t.stat_collection.get_attribute(AttributeId.STRENGTH).value, 7.5, "Did not apply flat agility debuff correctly")

        fsb = AttributeModifier(AttributeModType.FLAT, AttributeId.STRENGTH, 5, 1)
        t.stat_collection.get_attribute(AttributeId.STRENGTH).add_modifier(fsb)
        self.assertEqual(t.stat_collection.get_attribute(AttributeId.STRENGTH).value, 15, "Did not apply buffs in the correct order")
        # s2 = Sprite('mage', (4,7), (4,8))
        # s2.move_a_square()
        # self.assertEqual(s2.facing, (4,9), "4,6")
        # s3 = Sprite('mage', (0,0), (1,0))
        # s3.move_a_square()
        # self.assertEqual(s3.facing, (2,0), "4,6")
        # s4 = Sprite('mage', (0,0), (-1,0))
        # s4.move_a_square()
        # self.assertEqual(s4.facing, (-1,0), "4,6")
if __name__ == '__main__':
    unittest.main()