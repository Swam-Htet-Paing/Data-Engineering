import numpy as np

first_3days = [200, 180, 250]
next_3days = [0, 220, 270]

combined = np.concatenate([first_3days, next_3days])
combined = np.delete(combined, 3)
combined = np.append(combined, 300)

print(f"total revenue: {np.sum(combined)}")
print(f"cumulative revenue: {np.cumsum(combined)}")
print(f"increase and decrease in between consescuitve days \n {np.diff(combined)}")