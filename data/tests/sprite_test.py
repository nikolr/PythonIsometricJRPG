from data.sprite import DOWN, LEFT, RIGHT, UP, Sprite
from data.tile import Tile
import unittest

class TestProjection(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.map = []
        for i in range(14):
            row = []
            for j in range(14):
                row.append(Tile(i, j))
            cls.map.append(row)

    def setUp(self) -> None:
        self.s1 = Sprite('mage', (4,7), DOWN, self.map)
        self.s2 = Sprite('mage', (4,7), UP, self.map, [])
        self.s3 = Sprite('mage', (0,0), LEFT, self.map, [])
        self.w1 = Sprite('wolf', (1,0), LEFT, self.map, [])
        self.s4 = Sprite('mage', (0,0), RIGHT, self.map, [])

    def test_sprite_move_down(self):
        self.s1.move_a_square()
        self.assertEqual(self.s1.facing, (4,5), "down")

    def test_sprite_move_up(self):
        self.s2.move_a_square()
        self.assertEqual(self.s2.facing, (4,9), "up")

    def test_sprite_move_occupied(self):
        self.s3.move_a_square()
        self.assertEqual(self.s3.facing, (1,0), "occupied tile")

    def test_sprite_move_oob(self):
        self.s4.move_a_square()
        self.assertEqual(self.s4.facing, (-1,0), "out of bounds")

if __name__ == '__main__':
    unittest.main()