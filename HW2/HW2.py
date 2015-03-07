__author__ = 'ngilbert'
import numpy as np

class HW2:
    def __init__(self):
        self.TenXTen = None
        self.columns = None
        self.rows = None
        self.sliced_matrix = None
        self.normalized_matrix = None


    def create_TenXTen(self):
        self.TenXTen = np.arange(0,100).reshape((10,10))

    def write_to_file(self, TenXTen):
        np.savetxt("tenxten.txt",self.TenXTen,fmt='%d')

    def read_TenXTen(self):
        self.TenXTen = np.loadtxt("tenxten.txt",dtype=np.int32)

    def read_rows(self, fname):
        self.rows = np.loadtxt(fname, dtype=np.int32)
        if self.rows.min() < 1 or self.rows.max() > self.TenXTen.shape[0]:
            raise ValueError('Rows are out of bounds')

    def read_cols(self, fname):
        self.columns=np.loadtxt(fname,dtype=np.int32)
        if self.columns.min() < 1 or self.columns.max() > self.TenXTen.shape[1]:
            raise ValueError('Columns are out of bounds')

    def slice_TenXTen(self):
        self.sliced_matrix = self.TenXTen[self.rows[:,None],self.columns] # this is necessary as self.rows, self.columns only returns intersections - https://stackoverflow.com/questions/22927181/selecting-specific-rows-and-columns-from-numpy-array

    def normalize(self):
        maxVal = self.TenXTen.max()
        minVal = self.TenXTen.min()
        self.normalized_matrix = (self.TenXTen - minVal)/float((maxVal-minVal)) # note that float() is necessary to avoid integer division


    def find_mean(self):
        return np.mean(self.TenXTen)

    def find_median(self):
        return np.median(self.TenXTen)

    def find_std(self):
        return np.std(self.TenXTen)


if __name__ == '__main__': # note this allows us to include this file in the test_HW2.py without trying to evaluate the code below - this is important to prevent errors below (as in functions called but not yet implemented)
    hw2 = HW2()
    TenXTen = hw2.create_TenXTen()
    hw2.write_to_file(TenXTen)
    hw2.read_TenXTen()
    print "Full Matrix **************\n", hw2.TenXTen
    hw2.read_rows()
    hw2.read_cols()
    hw2.slice_TenXTen()
    print "Sliced Matrix *********\n", hw2.sliced_matrix
    hw2.normalize()
    print ("Normalized Matrix ****************\n",hw2.normalized_matrix)
    print "Mean**********\n", hw2.find_mean()
    print "Median*********\n",hw2.find_median()
    print "Standard Deviation********\n",hw2.find_std()
