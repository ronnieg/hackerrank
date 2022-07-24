# Enter your code here. Read input from STDIN. Print output to STDOUT
def symmetric_difference(a, b):
    lst = list(a.difference(b)) + list(b.difference(a))
    lst.sort()
    return "\n".join(str(x) for x in lst)


if __name__ == '__main__':
    m = int(input())
    a = set(list(map(int, input().split())))
    m = int(input())
    b = set(list(map(int, input().split())))
    print(symmetric_difference(a, b))


