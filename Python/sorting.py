num_cases = int(input())
total_moves = []

for i in range(num_cases):
    cur_moves = 0
    num_groups = int(input())
    papers_graded = input()
    grouped_grades = papers_graded.split()
    grouped_grades = list(map(int, grouped_grades))

    while(len(grouped_grades) > 1):
        min_val1 = min(grouped_grades)
        grouped_grades.remove(min_val1)
        min_val2 = min(grouped_grades)
        grouped_grades.remove(min_val2)
        grouped_grades.append(min_val1+min_val2)
        cur_moves += (min_val1+min_val2)

    total_moves.append(cur_moves)

for move in total_moves:
    print(move)
