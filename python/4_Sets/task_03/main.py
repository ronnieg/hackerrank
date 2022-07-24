# Enter your code here. Read input from STDIN. Print output to STDOUT
l = []
size = int(input())
for i in range(size):
    a = input()
    l.append(a)

print(len(set(l)))