def get_average(scores):
  total = 0
  count = 0
  for score in scores:
      total += score
      count += 1
  return round(total / count, 2)

def classify(avg):
  if avg >= 8.0:
      return "Excellent"
  elif avg >= 6.5:
      return "Good"
  elif avg >= 5.0:
      return "Average"
  else:
      return "Weak"

def class_report(students):
  report_data = []
  counts = {"Excellent": 0, "Good": 0, "Average": 0, "Weak": 0}

  for student in students:
    avg = get_average(student["scores"])
    cat = classify(avg)
    counts[cat] += 1
    report_data.append(
      {"name": student["name"], "avg": avg, "classification": cat}
    )
    print(f"{student['name']}: {avg} - {cat}")

  top_student = report_data[0]
  for s in report_data:
    if s["avg"] > top_student["avg"]:
      top_student = s

  print(f"Top student: {top_student['name']} ({top_student['avg']})")
  print(f"Excellent: {counts['Excellent']}")
  print(f"Good: {counts['Good']}")
  print(f"Average: {counts['Average']}")
  print(f"Weak: {counts['Weak']}")

  n = 0
  for _ in report_data:
    n += 1

  for i in range(n):
    for j in range(0, n - i - 1):
      if report_data[j]["avg"] < report_data[j + 1]["avg"]:
        report_data[j], report_data[j + 1] = (
          report_data[j + 1],
          report_data[j],
        )

  print("Ranking:")
  rank = 1
  for s in report_data:
    print(f"{rank}. {s['name']} - {s['avg']}")
    rank += 1


students = [
  {"name": "An", "scores": [8, 9, 10]},
  {"name": "Binh", "scores": [6, 7, 5]},
  {"name": "Chi", "scores": [7, 8, 7]},
  {"name": "Dung", "scores": [4, 5, 3]},
  {"name": "Hoa", "scores": [9, 8, 8]},
]

class_report(students)