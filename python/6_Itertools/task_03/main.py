# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement


line = list(map(str, input().split()))
string = line[0]
length = int(line[1])
comb = list(combinations_with_replacement(string, length))
empty_arr = []
for i in range(len(comb)):
    a = list(comb[i])
    a.sort()
    empty_arr.append(a)

empty_arr.sort()
for i in range(len(empty_arr)):
    print(''.join(empty_arr[i]))