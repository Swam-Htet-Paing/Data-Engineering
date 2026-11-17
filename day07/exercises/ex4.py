import re

emails = ["john@gmail.com", "mary@yahoo.com", "david@gmail", "anna@.com", "peter123@hotmail.com"]
for email in emails:
  if re.fullmatch(r"^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+$", email):
    print(f"Valid: {email}; ",end="")
  else:
    print(f"Invalid: {email}; ",end="")
