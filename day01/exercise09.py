def find_passed_students(students):
  for key, value in students.items():
    if value >= 50:
      print(f"{key}: {value}")

students = {
  "John": 75,
  "Mary": 45,
  "David": 80,
  "Anna": 55
}
find_passed_students(students)