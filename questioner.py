import random
import sys
import time
import os

def levenshtein_distance(s, t):
    m, n = len(s) + 1, len(t) + 1
    d = [[0] * n for _ in range(m)]

    for i in range(1, m):
        d[i][0] = i

    for j in range(1, n):
        d[0][j] = j

    for j in range(1, n):
        for i in range(1, m):
            substitution_cost = 0 if s[i - 1] == t[j - 1] else 1
            d[i][j] = min(d[i - 1][j] + 1,
                          d[i][j - 1] + 1,
                          d[i - 1][j - 1] + substitution_cost)

    return d[m - 1][n - 1]

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
    correct = all([True if a.lower() in answer.lower() else False for a in ans.split(' ')]) if len(ans.split(' ')) > 1 else ans.lower() == answer.lower()
    status = ""
    avglen = (len(answer) + len(ans)) / 2
    if correct:
        status = "Correct"
        used.append((question, answer))
    elif (len(ans) - len(answer)) / avglen < 0.25 and levenshtein_distance(ans, answer) / avglen < 0.3:
        status = "Close"
        used.append((question, answer))
    else:
        status = "Incorrect"
        exam.append((question, answer))
        random.shuffle(exam)
    print(f"{status}: {answer}")
    print(f"Questions left: {len(exam)}")
    finish = input("Would you like to continue (Y/N)? ").upper()