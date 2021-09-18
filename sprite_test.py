from sprite import Sprite
from tilemap import TileMap
from tile import Tile
import projection
import unittest
from sprite import Sprite
#Movement from (0,0) to (1,0) should increase world coordinates by tilewidth/2 in x and tileheight/2 in y

class TestProjection(unittest.TestCase):
    def test_sprite(self):
        #Ready the tilemap
        f = open('map_full.txt')
        read_map = [[int(c) for c in row] for row in f.read().split('\n')]
        f.close()
        map = []
        for y, row in enumerate(read_map):
            for x, index in enumerate(row):
                map.append(Tile(x, y))
        tilemap = TileMap(13, 13, map)
        s1 = Sprite('mage', (4,7), (4,6), tilemap, [])
        s1.move_a_square()
        self.assertEqual(s1.facing, (4,5), "down")
        s2 = Sprite('mage', (4,7), (4,8), tilemap, [])
        s2.move_a_square()
        self.assertEqual(s2.facing, (4,9), "up")
        s3 = Sprite('mage', (0,0), (1,0), tilemap, [])
        w1 = Sprite('wolf', (1,0), (2,0), tilemap, [])
        s3.move_a_square()
        self.assertEqual(s3.facing, (1,0), "occupied tile")
        s4 = Sprite('mage', (0,0), (-1,0), tilemap, [])
        s4.move_a_square()
        self.assertEqual(s4.facing, (-1,0), "out of bounds")
        self.assertEqual(s4.facing_tile, None, "out of bounds")
if __name__ == '__main__':
    unittest.main()