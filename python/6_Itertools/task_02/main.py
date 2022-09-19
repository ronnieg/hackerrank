# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations


line = list(map(str, input().split()))
string = line[0]
length = int(line[1])
lst = []
string = list(string)
string.sort()
string = ''.join(string)

for i in range(1, length + 1):
    a = list(combinations(string, i))

    for i in range(len(a)):
        tup = a[i]
        print(''.join(tup))