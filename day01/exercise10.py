def analyze_numbers(numbers):
  largest = numbers[0] 
  smallest = numbers[0]
  sum = 0
  even = 0
  odd = 0
  for i in range(len(numbers)):
    if numbers[i] > largest:
      largest = numbers[i]
    if numbers[i] < smallest:
      smallest = numbers[i]
    if numbers[i] % 2 == 0:
      even += 1
    else:
      odd += 1
    sum += numbers[i]
  avg = sum / len(numbers)
  print(f"Largest number: {largest}")
  print(f"Smallest number: {smallest}")
  print(f"Sum: {sum}")
  print(f"Average: {avg:.2f}")
  print(f"Even numbers: {even}")
  print(f"Odd numbers: {odd}")

analyze_numbers([12, 5, 8, 21, 30, 17, 4])