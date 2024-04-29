import random
import sys
import time
import os
import functools

@functools.lru_cache
def levenshteinRecursive(str1, str2, m, n):
      # str1 is empty
    if m == 0:
        return n
    # str2 is empty
    if n == 0:
        return m
    if str1[m - 1] == str2[n - 1]:
        return levenshteinRecursive(str1, str2, m - 1, n - 1)
    return 1 + min(
          # Insert     
        levenshteinRecursive(str1, str2, m, n - 1),
        min(
              # Remove
            levenshteinRecursive(str1, str2, m - 1, n),
          # Replace
            levenshteinRecursive(str1, str2, m - 1, n - 1))
    )

random.seed(time.time())

exam = []
used = []
if len(sys.argv) == 1:
    fn = [f for f in os.listdir('.') if f.endswith('.txt')]
else:
    fn = sys.argv[1:]

for f in fn:
    with open(f, "r", encoding="utf-8") as fin:
        for line in fin:
            part = line.strip().split(",")
            ans = [a.strip() for a in part[-1].split(" ")]
            part.pop(-1)
            question = [q.strip().split(" ") for q in part]
            for i in range(len(question)):
                for j in range(len(question[i])):
                    for a in ans:
                        if question[i][j].strip() == a:
                            question[i][j] = "___"
                            break
            question = ", ".join([" ".join(q) for q in question])
            ans = " ".join(ans).strip()
            used.append((question, ans))

finish = "Y"
while finish != "N":
    if len(exam) == 0:
        exam = used
        random.shuffle(exam)
        used = []
    question, answer = exam.pop()
    print(question)
    ans = input("Answer: ").lower().strip()
    correct = all([True if a.lower() in answer.lower() else False for a in ans.split(',')]) if len(ans) else False
    status = ""
    if correct:
        status = "Correct"
        used.append((question, answer))
    elif levenshteinRecursive(ans.lower(), answer.lower(), len(ans), len(answer)) / len(answer) < 0.3:
        status = "Close"
        used.append((question, answer))
    else:
        status = "Incorrect"
        exam.append((question, answer))
        random.shuffle(exam)
    print(len(exam))
    print(f"{status}: {answer}")
    finish = input("Would you like to continue (Y/N)? ").upper()