import numpy as np

arr = np.array([10, 20, 30, 40, 50])
arr[0] = 100
arr[2] = 300
arr[-1] = 500
arr[1:3] = 0
print(arr)