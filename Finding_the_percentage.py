if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result=0
    if query_name in student_marks:
        # print(student_marks[query_name])
        for i in range(len(student_marks[query_name])):
            result+=float(student_marks[query_name][i])
            print(student_marks[query_name][i])
        print("%.2f"%float(result/3))
