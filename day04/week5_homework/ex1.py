import numpy as np

temp_arr = np.array([31, 27, 34, 29, 26, 33, 30])
print(f"Temperature values in ascending order: {np.sort(temp_arr)}")
print(f"Temperature values in descending order: {-1 * np.sort(-temp_arr)}")
print(f"Highest tempereature: {np.max(temp_arr)}, index: {np.argmax(temp_arr)}")
print(f"Lowest temperature: {np.min(temp_arr)}, index: {np.argmin(temp_arr)}")