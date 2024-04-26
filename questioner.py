import random
import sys
import time

random.seed(time.time())

exam = []
used = []

with open(sys.argv[1], "r", encoding="utf-8") as fin:
    for line in fin:
        part = line.strip().split(",")
        ans = part[-1].split(" ")
        part.pop(-1)
        question = ",".join(part).split(" ")
        for i in range(len(question)):
            for a in ans:
                if question[i] == a:
                    question[i] = "___"
                    break
        question = " ".join(question).strip()
        ans = " ".join(ans).strip()
        used.append((question, ans))

finish = "Y"
while finish != "N":
    if len(exam) == 0:
        exam = used
        random.shuffle(exam)
        used = []
    question, answer = exam.pop()
    used.append((question, answer))
    print(question)
    ans = "".join(input("Answer: ").strip().split(','))
    print(f"{'Correct' if ans.lower() == answer.lower() else 'Incorrect'}: {answer}")
    finish = input("Would you like to continue (Y/N)? ").upper()