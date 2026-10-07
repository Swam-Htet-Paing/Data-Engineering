scores = []
with open("scores.txt", "r") as file:
  for line in file:
    scores.append(float(line.strip()))
  
  max_score = scores[0]
  for score in scores:
    if score >= max_score:
      max_score = score

  print(f"Highest score: {max_score}")