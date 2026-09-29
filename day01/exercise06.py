def count_even(numbers):
  count = 0
  for number in numbers:
    if number % 2 == 0:
      count += 1
  print(f"Number of even numbers: {count}")
count_even([10, 15, 22, 31, 40, 55])
  