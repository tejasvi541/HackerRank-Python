if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = 0
    for i in range(0, 3):
        sum += int(student_marks[query_name].pop())
    average = sum/3
    print(format(average,'.2f'))
