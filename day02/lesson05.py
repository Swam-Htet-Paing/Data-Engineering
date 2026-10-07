file = open("scores.txt", "r")
count = 0
total = 0

for score in file:
  count += 1
  total += int(score.strip())

avg = total / count
print(f"Total: {total}")
print(f"Average: {avg}")
file.close()