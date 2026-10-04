def is_leap_year(year):
  if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    return True
  return False

year = 2024
if is_leap_year(year):
  print(f"{year} is a leap year. February has 29 days.")
else:
  print(f"{year} is not a leap year. February has 28 days.")