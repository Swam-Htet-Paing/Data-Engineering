import re

text = "Python is Easy and I Love Programming"
print(re.findall(r"\bis\b|\band\b", text))