import unittest
from HW2 import HW2
import numpy as np

__author__ = 'John'


class TestHW2(unittest.TestCase):
    def test_create_TenXTen(self):
        # Arrange: Create a new HW2 object
        hw = HW2()
        # Act: Call create_TenXTen on the HW2 object and assign resulting matrix to TenXTen
        hw.create_TenXTen()
        TenXTen = hw.TenXTen
        #Assert: Verify that the result is size 10 x 10
        self.assertEqual(np.shape(TenXTen), (10, 10))

    def test_slice_TenXTen(self):
        # Arrange: Create a new hw2 object
        hw2 = HW2()
        # Act: Create a TenXTen matrix, slice it and set the results to sliced
        hw2.create_TenXTen()
        hw2.read_cols()
        hw2.read_rows()
        hw2.slice_TenXTen()
        sliced = hw2.sliced_matrix
        # Assert: Assert that the size of sliced is 4x4
        self.assertEqual(np.shape(sliced),(4,4))

if __name__ == '__main__':
    unittest.main()