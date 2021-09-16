from sprite import Sprite
from projection import Projection
import unittest
from sprite import Sprite
#Movement from (0,0) to (1,0) should increase world coordinates by tilewidth/2 in x and tileheight/2 in y

class TestProjection(unittest.TestCase):
    def test_isometricprojeciton(self):
        # s1 = Sprite('mage', (4,7), (4,6))
        # s1.move_a_square()
        # self.assertEqual(s1.facing, (4,5), "4,6")
        # s2 = Sprite('mage', (4,7), (4,8))
        # s2.move_a_square()
        # self.assertEqual(s2.facing, (4,9), "4,6")
        # s3 = Sprite('mage', (0,0), (1,0))
        # s3.move_a_square()
        # self.assertEqual(s3.facing, (2,0), "4,6")
        s4 = Sprite('mage', (0,0), (-1,0))
        s4.move_a_square()
        self.assertEqual(s4.facing, (-1,0), "4,6")
if __name__ == '__main__':
    unittest.main()