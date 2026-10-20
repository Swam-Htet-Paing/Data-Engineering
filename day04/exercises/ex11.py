import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

arr[:, 0] = 100
arr[1] = 0
arr[2, 2] = 999

print(arr)