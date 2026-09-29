def calculate_average(scores):
  total = 0
  for score in scores:
    total += score
  avg = total / len(scores)
  print(f"Average score: {avg}")
calculate_average([8, 7, 9, 6, 10])