import os


# Complete the solve function below.
def solve(s):
    l = []
    n = s.split(" ")
    for i in n:
        l.append(i.capitalize())
    s = " ".join(str(x) for x in l)
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
