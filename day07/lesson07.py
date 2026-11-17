students = [
    "John - 0912345678",
    "Mary - 0987654321",
    "David - ABC123",
    "Anna - 0901234567",
    "Peter - 12345"
]

import re

text = "A123 B45 C6789"
result = re.findall(r"\d+", text) # \d = a digit, \d+ = one or more digits
print(result) # ['123', '45', '6789']

'''
anchors
^ start of string
$ end of string
'''
phone = "0912345678"
pattern = r"^\d{10}$" # only 10 digits from start to end
if re.search(pattern, phone):
  print("Valid phone number")
else:
  print("Invalid phone number")

# demo 1: find all numbers in a sentence
text = "I have 2 books, 10 pens and 5 notebooks"
numbers = re.findall(r"\d+", text)
print("Numbers: ", numbers)

# demo 2: final all email addresses
text = """
Contact us:
john@gmail.com
mary@yahoo.com
david@company.org
"""
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(pattern, text)
for email in emails:
  print(email)

# demo 3: checks if a phone number has exactly 10 digits
# phone = input("Enter your phone number: ")
# pattern = r"^[0-9]{10}$"
# if re.fullmatch(pattern, phone):
#   print("Valid phone number")
# else:
#   print("Invalid phone number")

# demo 4: replace all digits with *
text = "My phone number is 0987123456"
result = re.sub(r"\d", "*", text)
print(result)

# demo 5: find words starting with a capital letter
text = "John studies Python at Van Lang University"
pattern = r"\b[A-Z][a-z]*\b" # \b marks boundary
words = re.findall(pattern, text)
print(words)