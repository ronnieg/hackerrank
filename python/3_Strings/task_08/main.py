# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split())

symbol = ".|."
dash = "-"
lst = []
welcome = "WELCOME".center(M, dash)
up = int((N - 1) / 2)
for i in range(1, up + 1):
    string = str(symbol * int(2 * i - 1)).center(M, dash)
    lst.append(string)


new_lst = lst + [welcome] + list(reversed(lst))

print("\n".join(new_lst))
