def find_max(a, b, c):
  if (a >= b and a >= c):
    print(f"The largest number is {a}.")
  elif (b >= a and b >= c):
    print(f"The largest number is {b}.")
  else:
    print(f"The largest number is {c}.")
find_max(15, 28, 20)