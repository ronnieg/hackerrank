# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
rez = list(product(line1, line2))
print(' '.join(map(str,rez)))
