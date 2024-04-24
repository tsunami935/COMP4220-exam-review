import random

exam = []

with open("exam2.txt", "r", encoding="utf-8") as fin:
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
        exam.append((question, ans))

finish = "Y"
while finish != "N":
    question, answer = random.choice(exam)
    print(question)
    ans = input("Answer: ").strip()
    print(f"{'Correct' if ans.lower() == answer.lower() else 'Incorrect'}: {answer}")
    finish = input("Would you like to continue (Y/N)? ").upper()