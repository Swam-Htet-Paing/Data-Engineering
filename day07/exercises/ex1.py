import re

text = "I bought 3 apples, 5 oranges and 12 bananas"
print(re.findall(r"\d+", text))
