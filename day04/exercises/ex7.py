import numpy as np

scores = np.array([65, 80, 75, 90, 55, 85, 95])
print(np.sum(scores))
print(np.mean(scores))
print(np.max(scores))
print(np.min(scores))
print(scores[scores>=80].size)