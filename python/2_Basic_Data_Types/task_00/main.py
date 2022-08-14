if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scopes = []

    for i in range(len(students)):
        scopes.append(students[i][1])

    scopes = list(set(scopes))
    scopes.sort()


    result = []

    for i in range(len(students)):
        if scopes[1] == students[i][1]:
            result.append(students[i][0])

    result.sort()
    print(*result, sep="\n")




