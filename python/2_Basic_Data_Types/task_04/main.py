if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        command = input().split()
        if "insert" == str(command[0]):
            lst.insert(int(command[1]), int(command[2]))

        if "print" == str(command[0]):
            print(lst)

        if "remove" == str(command[0]):
            lst.remove(int(command[1]))

        if "append" == str(command[0]):
            lst.append(int(command[1]))

        if "sort" == str(command[0]):
            lst.sort()

        if "pop" == str(command[0]):
            lst.pop()

        if "reverse" == str(command[0]):
            lst.reverse()
