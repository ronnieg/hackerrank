# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
lst = []
for i in range(t):
    count_of_a = int(input())
    a = set(map(int, input().split()))
    count_of_b = int(input())
    b = set(map(int, input().split()))
    lst.append(a.issubset(b))

for i in range(len(lst)):
    print(lst[i])