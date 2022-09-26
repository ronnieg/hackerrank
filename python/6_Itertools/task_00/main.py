# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

a = list(map(str, input().split()))
W = list(a[0])
W.sort()
L = list(permutations(W, int(a[1])))
for i in range(len(L)):
    tup = L[i]
    print(''.join(tup))