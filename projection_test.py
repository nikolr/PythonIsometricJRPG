from projection import Projection
import unittest
from projection import Projection
#Movement from (0,0) to (1,0) should increase world coordinates by tilewidth/2 in x and tileheight/2 in y

class TestProjection(unittest.TestCase):
    def test_isometricprojeciton(self):
        # self.assertEqual(Projection.isometricprojection(0,0,32,16), (0,0), "Origo")
        # self.assertEqual(Projection.isometricprojection(1,0,32,16), (16,8), "1 left")
        # self.assertEqual(Projection.isometricprojection(0,1,32,16), (-16,8), "1 right")
        # self.assertEqual(Projection.isometricprojection(2,1,32,16), (16,24), "2 left 1 down")

        # self.assertEqual((0, 0), Projection.reverse_isometricprojection(0,0,32,16), "Origo")
        # self.assertEqual((1, 0), Projection.reverse_isometricprojection(16,8,32,16), "1")
        # self.assertEqual((0, 1), Projection.reverse_isometricprojection(-16,8,32,16), "2")
        # self.assertEqual((2, 1), Projection.reverse_isometricprojection(16,24,32,16), "3")

        # self.assertEqual(Projection.ranges(0,0,32,16), (-16,16), "Origo")
        # self.assertEqual(Projection.ranges(1,0,32,16), (16,8), "1 left")
        # self.assertEqual(Projection.ranges(0,1,32,16), (-16,8), "1 right")
        # self.assertEqual(Projection.ranges(2,1,32,16), (16,24), "2 left 1 down")

        #test adjecant tile list
        self.assertEqual(Projection.get_adjecant_squares(0,0,4), [(0,1), (1,0), (1,1)], "Origo")
        self.assertEqual(Projection.get_adjecant_squares(1,1,4), [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2)], "1, 1")


        self.assertEqual(Projection.get_orthogonal_adjecant_squares(1,1,2), [(0,1), (1,0), (2,1), (1,2)], "ort sq")
        self.assertEqual(Projection.get_orthogonal_adjecant_squares(0,0,2), [(1,0), (0,1)], "ort sq")

if __name__ == '__main__':
    unittest.main()
