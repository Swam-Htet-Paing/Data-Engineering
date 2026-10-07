scores = []
file = open("scores.txt", 'r')
for line in file:
  scores.append(float(line))

count = 0
for score in scores:
  if score >= 5.0:
    count += 1

print(f"Passed students: {count}")
print(f"Failed students: {len(scores) - count}")
file.close()