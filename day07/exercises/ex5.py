import re

text = "John: 0912345678; Mary: 0987654321; David: 12345; Anna: 0901234567; Peter: 09123ABC45"
# print(re.findall(r"\b[0-9|\D]{10}\b", text))
print(re.findall(r"\b[0-9]{10}\b", text))