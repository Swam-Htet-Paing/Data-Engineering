import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))