# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
n_array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0


# print(n, m)
# print(n_array)
# print(A)
# print(B)

for i in range(len(n_array)):
    if n_array[i] in A:
        happiness += 1
    if n_array[i] in B:
        happiness -= 1

print(happiness)

