import math

num_cases = int(input())
total_pages = []

for i in range(num_cases):
    required_paper = []
    diff_exams = int(input())
    for j in range(diff_exams):
        info = input()
        num_students = int(info.split()[0])
        num_pages = int(info.split()[1])
        num_paper = int(math.ceil(num_pages / 4.0))
        required_paper.append(num_paper*num_students)
    total_pages.append(sum(required_paper))

for page_count in total_pages:
    print(page_count)
