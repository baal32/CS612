import numpy as np

test = np.arange(0,100).reshape(10,10)
print test
rows = [3,5,7,9]
fuckoffpython = np.array(rows)
cols = [2,4,6,8]
#print test[rows]
#print test[:,cols]
print test[fuckoffpython[:,None],cols]
#print test[(1,2,3,4,5),(1,2,3,4,5)]
