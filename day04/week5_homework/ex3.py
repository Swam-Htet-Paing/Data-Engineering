import numpy as np

arr = [3, 7, 3, 9, 7, 3, 5, 9, 3]
values, counts = np.unique(arr, return_counts=True)
most_frequent = values[np.argmax(counts)]

print(f"Unique values: {values}")
print(f"Occurrences: {counts}")
print(f"Most frequent value: {most_frequent}")