__author__ = 'ngilbert'

import numpy as np

class HW1:

    def __init__(self):
        self.OneD = None
        self.TwoD = None
        self.SortOneD = None
        self.array1 = None
        self.array2 = None
        self.array3 = None

    def readFromFileIntoArray(self, fname):
        self.OneD =  np.loadtxt(fname, dtype=np.int32)

    def printOneD(self):
        print self.OneD

    def createRandomTwoD(self, low, high, dim1, dim2):
        self.TwoD = np.random.random_integers(low, high, (dim1,dim2))

    def sortOneD(self):
        self.SortOneD = np.sort(self.OneD)

    def splitTwoD(self, splits):
        self.array1 = self.TwoD[:splits[0][0], :splits[0][1]]
        self.array2 = self.TwoD[:splits[1][0], splits[0][1]:splits[0][1] + splits[1][1]]
        self.array3 = self.TwoD[:splits[2][0], splits[0][1]+splits[1][1]: splits[0][1]+splits[1][1]+splits[2][1]]

    def printTwoD(self):
        print self.TwoD

    def printSortOneD(self):
        print self.SortOneD

    def writeArraysToFile(self):
        np.savetxt("File1",self.array1, fmt='%d')
        np.savetxt("File2",self.array2, fmt='%d')
        np.savetxt("File3",self.array3, fmt='%d')


def Main():

    hw1 = HW1()
    hw1.readFromFileIntoArray("intfile.txt")
    hw1.printOneD()

    hw1.createRandomTwoD(0,99,5,5)
    hw1.printTwoD()

    hw1.sortOneD()
    hw1.printSortOneD()

    hw1.splitTwoD([(5,2),(5,2),(5,1)])

    hw1.writeArraysToFile()

    print hw1.array1
    print hw1.array2
    print hw1.array3

Main()