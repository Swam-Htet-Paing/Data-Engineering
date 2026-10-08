total = 0.0
count = 0

with open("scores.txt", "r") as f:
  scores = f.read().split()
  for s in scores:
    total += float(s)
    count += 1

avg = total / count
print(f"Average score: {avg}")