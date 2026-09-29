def display_student(student):
  print(f"Name : {student["name"]}")
  print(f"Age : {student["age"]}")
  print(f"Major : {student["major"]}")
  print(f"Score : {student["score"]}")

student = {
  "name": "John",
  "age": 20,
  "major": "Information Technology",
  "score": 85
}
display_student(student)