# Enter your code here. Read input from STDIN. Print output to STDOUT
superset = set(map(int, input().split()))
count_of_other_sets = int(input())
lst = []

for i in range(count_of_other_sets):
    n_set = set(map(int, input().split()))
    lst.append(superset.issuperset(n_set))

lst = list(set(lst))
for i in range(len(lst)):
    if False == lst[i]:
        print("False")
        break
    else:
        print("True")
