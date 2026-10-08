a = 0
b = 0
c = 0
d = 0
f_grade = 0

with open("scores.txt", "r") as f:
  scores = f.read().split()
  for s in scores:
    score = float(s)
    if score >= 8.5:
      a += 1
    elif score >= 7.0:
      b += 1
    elif score >= 5.5:
      c += 1
    elif score >= 4.0:
      d += 1
    else:
      f_grade += 1

print(f"Grade A: {a} Grade B: {b} Grade C: {c} Grade D: {d} Grade F: {f_grade}")