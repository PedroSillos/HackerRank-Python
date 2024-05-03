students = list()
names = list()
scores = list()

for s in range( int(input()) ):
    name = input()
    score = float(input())
    students.append([name,score])
    names.append(name)
    scores.append(score)

sec_low = max(scores)

for score in scores:
    if score < sec_low and score != min(scores):
        sec_low = score

for name in sorted(names):
    for student in students:
        if student[0] == name and student[1] == sec_low:
            print(student[0])