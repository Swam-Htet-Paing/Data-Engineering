import numpy as np
scores = np.array([70, 80, 90, 95])
print(scores)
print(scores + 10) # adds 10 to every element

arr = np.zeros(5)
print(arr)

arr = np.ones(4)
print(arr)

arr = np.arange(1,10)
print(arr)

arr = np.arange(0, 11, 2)
print(arr)

arr = np.linspace(0, 10, 5)
print(arr)

arr = np.random.randint(1, 101, size=5)
print(arr)

print(arr[0])
print(arr[2])
print(arr[-1])

arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[1:4])
print(arr[:3])
print(arr[3:])
print(arr[::2])

print(arr + 5)
print(arr - 5)
print(arr * 2)
print(arr / 10)
print(arr ** 2)

print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)

print(np.sum(arr))
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.std(arr))

scores = np.array([45, 60, 75, 85, 95])
print(scores >= 70)
print(scores[scores >= 70])

arr = np.array([
  [10, 20, 30],
  [40, 50, 60]
])
print(arr)

arr = np.zeros((2, 3))
print(arr)

arr = np.ones((3, 2))
print(arr)

arr = np.arange(1, 13).reshape(3, 4)
print(arr)

arr = np.random.randint(1, 10, size=(2,3))
print(arr)

arr = np.array([
  [10, 20, 30],
  [40, 50, 60],
  [70, 80, 90]
])

print(arr[0,0])
print(arr[1,2])
print(arr[2,1])

# print rows
print(arr[0])
print(arr[1])

# print columns
print(arr[:,0])
print(arr[:,1])

print(arr[0:2, 1:3])

arr[1, 1] = 999
print(arr)

arr[0] = 0
print(arr)

arr[:, 0] = 100
print(arr)

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))