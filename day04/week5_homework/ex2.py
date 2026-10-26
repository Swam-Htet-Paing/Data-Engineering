import numpy as np

arr = np.array([42, 67, 85, 51, 73, 98, 60, 39, 80])
numbers = arr[(arr > 50) & (arr <=80)]
print(numbers)
print(numbers.size)
print(np.mean(numbers))