scores = []
with open("scores.txt", "r") as file:
  for line in file:
    scores.append(float(line.strip()))
  
  min_score = scores[0]
  for score in scores:
    if score <= min_score:
      min_score = score

  print(f"Lowest score: {min_score}")