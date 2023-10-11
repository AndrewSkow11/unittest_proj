import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([], 0), None)
        self.assertEqual(arrs.get([], -5), None)
        self.assertEqual(arrs.get([1, 2, 3], -5), None)
        self.assertEqual(arrs.get([1,2,3,5,8], 4), 8)



    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 0), [1, 2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1, -2), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -1, -2), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -2), [2,3])


    def test_slice_new(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 890),[2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -1234, 890), [1, 2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 0, 0), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -1, 0), [])
        self.assertEqual(arrs.my_slice([], -1, 0), [])

