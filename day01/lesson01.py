name = "John"
age = 20
score = 85
is_student = True

# Dynamic typed
x = 10
x = "Python"

a, b = 10, 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(age>=18)

if age >= 18:
  print("You are an adult")
else:
  print("You are under 18")

if score >= 90:
  print("A")
elif score >= 80:
  print("B")
elif score >= 70:
  print("C")
else:
  print("D")

for i in range(5):
  print("Hello")

i = 0
while(i<5):
  print(i)
  i += 1

fruits = ["apple", "banana", "orange"]
student = ["John", 20, 8.5]
print(fruits[0])
print(fruits[1])

fruits[1] = "mango"
fruits.append("grape")
fruits.remove("apple")

student = {
  "name" : "John",
  "age" : 20,
  "score" : 8.5
}

print(student["name"])
print(student["score"])

def greeting():
  print("Hello, everyone!")
greeting()

def greeting(name):
  print("Hello ", name)
greeting("John")
greeting("Mary")

def add(a, b):
  return a + b

result = add(10, 20)
print(result)