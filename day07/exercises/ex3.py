import re

ids = ["AB1234", "XY5678", "ab1234", "ABC1234", "AB123"]
pattern = r"^[A-Z]{2}\d{4}$"
for id in ids:
  if re.fullmatch(pattern, id):
    print(f"{id} Valid; ",end="")
  else:
    print(f"{id} Invalid; ",end="")
