with open("scores.txt", "r") as infile, open("result.txt", "w") as outfile:
  scores = infile.read().split()
  for s in scores:
    score = float(s)
    status = "Pass" if score >= 5.0 else "Fail"
    outfile.write(f"{score} - {status}\n")