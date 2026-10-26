import numpy as np

scores =  [8.34, 10.5, -1, 6.48, 4.96, 7, 3.21]
processed_scores = np.round(np.clip(scores, 0, 10), decimals=1)
print(f"grades limited between 0-10, up to 1 decmial place\n {processed_scores}")
grades = []

for score in processed_scores:
  if score >= 8.0:
    grades.append('Excellent')
  elif score >= 6.5:
    grades.append('Good'),
  elif score >= 5.0:
    grades.append('Average')
  else:
    grades.append('Weak')

grades = np.array(grades)
print(f"classified grades: {grades}")