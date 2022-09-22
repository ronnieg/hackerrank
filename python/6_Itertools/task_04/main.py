# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
S = input()
for k, g in groupby(str(S)):
    print('({}, {})'.format(len(list(g)), k), end=" ")
