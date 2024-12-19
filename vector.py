import unittest


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def length2(self):
        return (self.x * self.x + self.y * self.y)


class VectorTestCase(unittest.TestCase):
    def test_add_zero(self):
        self.assertEqual(Vector(3, 4) + Vector(0, 0), Vector(3, 4))
    
    def test_add_one(self):
        self.assertEqual(Vector(3, 4) + Vector(1, 1), Vector(4, 5))

    def test_add_two_three(self):
        self.assertEqual(Vector(3, 4) + Vector(2, 3), Vector(5, 7))


    def test_sub_1(self):
        self.assertEqual(Vector(3, 4) - Vector(2, 3), Vector(1, 1))

    def test_sub_2(self):
        self.assertEqual(Vector(2, 3) - Vector(3, 4), Vector(-1, -1))

    def test_sub_3(self):
        self.assertEqual(Vector(3, 4) - Vector(0, 0), Vector(3, 4))
        

    def test_length2_1(self):
        v = Vector(3, 4)
        self.assertEqual(v.length2(), (3 * 3 + 4 * 4))
    
    def test_length2_2(self):
        v = Vector(10, 12)
        self.assertEqual(v.length2(), (10 * 10 +12 * 12))

    def test_length2_3(self):
        v = Vector(-1, -10)
        self.assertEqual(v.length2(), ((-1) * (-1) + (-10) * (-10)))
    

    def test_eq_true(self):
        v1, v2 = Vector(3, 4), Vector(3, 4)
        self.assertTrue(v1 == v2)

    def test_eq_false1(self):
        v1, v2 = Vector(3, 4), Vector(3, 5)
        self.assertFalse(v1 == v2)
    
    def test_eq_false2(self):
        v1, v2 = Vector(-1, -1), Vector(1, 1)
        self.assertFalse(v1 == v2)

    def test_eq_false3(self):
        v1, v2 = Vector(1, 1), Vector(2, 1)
        self.assertFalse(v1 == v2)
