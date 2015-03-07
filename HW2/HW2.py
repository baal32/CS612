__author__ = 'ngilbert'
import numpy as np

class HW2:
    def __init__(self):
        self.TenXTen = None
        self.columns = None
        self.rows = None
        self.sliced_matrix = None


    def create_TenXTen(self):
        self.TenXTen = np.arange(0,100).reshape((10,10))

    def write_to_file(self, TenXTen):
        np.savetxt("tenxten.txt",self.TenXTen,fmt='%d')

    def read_TenXTen(self):
        self.TenXTen = np.loadtxt("tenxten.txt",dtype=np.int32)

    def read_rows(self):
        self.rows = np.loadtxt("rows.txt", dtype=np.int32)

    def read_cols(self):
        self.columns=np.loadtxt("columns.txt",dtype=np.int32)

    def slice_TenXTen(self):
        self.sliced_matrix = self.TenXTen[self.rows[:,None],self.columns] # this is necessary as self.rows, self.columns only returns intersections - https://stackoverflow.com/questions/22927181/selecting-specific-rows-and-columns-from-numpy-array

    def print_sliced_matrix(self):
        print self.sliced_matrix

    def normalize(self):
        pass

    def find_mean(self):
        pass

    def find_median(self):
        pass

    def find_std(self):
        pass


if __name__ == '__main__': # note this allows us to include this file in the test_HW2.py without trying to evaluate the code below - this is important to prevent errors below (as in functions called but not yet implemented)
    hw2 = HW2()
    TenXTen = hw2.create_TenXTen()
    hw2.write_to_file(TenXTen)
    hw2.read_TenXTen()
    hw2.read_rows()
    hw2.read_cols()
    hw2.slice_TenXTen()
    hw2.print_sliced_matrix()
    hw2.normalize()
    hw2.find_mean()
    hw2.find_median()
    hw2.find_std()
    hw2.dosomethingfake()
