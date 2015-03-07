import unittest
from unittest import TestCase
from HW2 import HW2
import numpy as np

__author__ = 'ngilbert'
# Arrange:
# Act:
# Assert:

class TestHW2(unittest.TestCase):
    def test_create_TenXTen(self):
        # Arrange: Create a new HW2 object
        hw = HW2()
        # Act: Call create_TenXTen on the HW2 object and assign resulting matrix to TenXTen
        hw.create_TenXTen()
        TenXTen = hw.TenXTen
        # Assert: Verify that the result is size 10 x 10
        self.assertEqual(np.shape(TenXTen), (10, 10))

    def test_slice_TenXTen(self):
        # Arrange: Create a new hw2 object
        hw2 = HW2()
        # Act: Create a TenXTen matrix, slice it and set the results to sliced
        hw2.create_TenXTen()
        hw2.read_cols("columns.txt")
        hw2.read_rows("rows.txt")
        hw2.slice_TenXTen()
        sliced = hw2.sliced_matrix
        # Assert: Assert that the size of sliced is 4x4
        self.assertEqual(np.shape(sliced), (4, 4))

    def test_normalize(self):
        # Arrange: create a new hw2 object
        hw2 = HW2()
        #Act: Call reate_TenXTen and normalize
        hw2.create_TenXTen()
        hw2.normalize()
        normalized = hw2.normalized_matrix
        #Assert: Assert that the max value of the normalized matrix is < 1
        self.assertLessEqual(normalized.max(), 1)

    def test_read_rows(self):
        # Arrange:  create a new hw2 object
        hw2 = HW2()
        hw2.create_TenXTen()
        # Act: Read the row indices from rows.txt
        hw2.read_rows("rows.txt")
        rows = hw2.rows
        # Assert:
        self.assertEqual(rows.size,4)

    def test_read_cols(self):
        # Arrange: create a new hw2 object
        hw2 = HW2()
        hw2.create_TenXTen()
        # Act: read the column indices from columns.txt
        hw2.read_cols("columns.txt")
        columns = hw2.columns
        # Assert:
        self.assertEqual(columns.size,4)

    def test_find_mean(self):
        # Arrange: create a new hw2 object
        hw2 = HW2()
        hw2.create_TenXTen()
        # Act: call find_mean and assign value to mean
        mean = hw2.find_mean()
        # Assert: assert that mean is 49.5
        self.assertEqual(mean,49.5)

    def test_find_median(self):
        # Arrange: create a new hw2 object
        hw2 = HW2()
        hw2.create_TenXTen()
        # Act: call find_median and assign value to median
        median = hw2.find_median()
        # Assert: assert that mean is 49.5
        self.assertEqual(median,49.5)

    def test_find_std(self):
        # Arrange: create a new hw2 object
        hw2 = HW2()
        hw2.create_TenXTen()
        # Act: call find_std and assign value to std
        std = hw2.find_std()
        # Assert: assert that mean is 49.5
        self.assertEqual("{0:.6f}".format(std),"{0:.6f}".format(28.8660700477))

if __name__ == '__main__':
    unittest.main()