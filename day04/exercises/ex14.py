import numpy as np

arr = np.arange(1,13)
arr = arr.reshape((3,4))
print(arr.shape)
arr = arr.reshape((4,3))
print(arr.shape)
arr = arr.reshape((2,6))
print(arr.shape)

# a 1 dimensional array can be reorganized as 2d arrays
# with rows and columns consisitng of the multiples of its total number of elements
# multiples of 12 are 2x6, 3x4, 4x3, 12x1 and etc.
