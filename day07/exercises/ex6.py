import re

text = "Python     is      very       interesting."
processed = re.sub(r"\s+", " ", text)
print(processed)