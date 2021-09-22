import projection
import unittest

#Movement from (0,0) to (1,0) should increase world coordinates by tilewidth/2 in x and tileheight/2 in y

class TestProjection(unittest.TestCase):
    def test_isometricprojection(self):
        self.assertEqual(projection.isometricprojection(0,0,32,16, 0, 0), (0,0), "Origo")
        self.assertEqual(projection.isometricprojection(1,0,32,16, 0, 0), (16,8), "1 left")
        self.assertEqual(projection.isometricprojection(0,1,32,16, 0, 0), (-16,8), "1 right")
        self.assertEqual(projection.isometricprojection(2,1,32,16, 0, 0), (16,24), "2 left 1 down")

    def test_reverse_isometricprojection(self):
        self.assertEqual((0, 0), projection.reverse_isometricprojection(0,0,32,16), "Origo")
        self.assertEqual((1, 0), projection.reverse_isometricprojection(16,8,32,16), "1")
        self.assertEqual((0, 1), projection.reverse_isometricprojection(-16,8,32,16), "2")
        self.assertEqual((2, 1), projection.reverse_isometricprojection(16,24,32,16), "3")

    def test_get_adjecant_squares(self):
        #test adjecant tile list
        self.assertEqual(projection.get_adjecant_squares(0,0,4), [(0,1), (1,0), (1,1)], "Origo")
        self.assertEqual(projection.get_adjecant_squares(1,1,4), [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2)], "1, 1")

    def test_get_orthogonal_adjecant_squares(self):
        self.assertEqual(projection.get_orthogonal_adjecant_squares(1,1,2), [(0,1), (1,0), (2,1), (1,2)], "ort sq")
        self.assertEqual(projection.get_orthogonal_adjecant_squares(0,0,2), [(1,0), (0,1)], "ort sq")
        self.assertEqual(projection.get_orthogonal_adjecant_squares(13,13,13), [(12,13), (13,12)], "ort sq")
    def test_get_distance(self):
        self.assertEqual(projection.get_distance((1,1), (2,2)), 2, "Distance should be two")
        self.assertEqual(projection.get_distance((1,1), (2,3)), 3, "Distance should be three")
        self.assertEqual(projection.get_distance((0,1), (0,11)), 10, "Distance should be ten")
        self.assertEqual(projection.get_distance((3,4), (7,0)), 8, "Distance should be eight")
    def test_get_closest(self):
        self.assertEqual(projection.get_closest((0, 0), [(12,12), (3,3), (3,4)]), (3,3), "Did not return closest")
        self.assertEqual(projection.get_closest((4, 3), [(12,12), (3,3), (3,4), (0, 0), (5,7)]), (3,3), "Did not return closest")
    def test_get_line(self):
        self.assertEqual(projection.get_line((0, 0), (1, 0)), [(0, 0), (1, 0),(2, 0), (3, 0),(4, 0), (5, 0),(6, 0), (7, 0),(8, 0), (9, 0), (10, 0), (11, 0), (12, 0)])
    def test_get_lines(self):
        self.assertEqual(projection.get_lines((0, 0)), [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12)] )

if __name__ == '__main__':
    unittest.main()
