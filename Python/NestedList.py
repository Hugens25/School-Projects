students = []
student_names = []
student_scores = []
second_place = []

names = ["Harsh","Beria","Varun","Kakunami","Vikas"]
scores = [20,20,19,19,21]

for i in range(5):
    name = names[i]
    score = scores[i]
    students.append([name, score])
    student_names.append(name)
    student_scores.append(score)

minimum_value = min(student_scores)
print(students)
for student in students:
    print("Checking {}".format(student))
    if student[1] == minimum_value:
        #students.remove(student)
        student_scores.remove(minimum_value)

minimum_value = min(student_scores)
for student in students:
    if student[1] == minimum_value:
        second_place.append(student[0])

s = sorted(set(second_place))

for element in s:
    print(element)
