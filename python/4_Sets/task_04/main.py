n = int(input())
s = set(map(int, input().split()))

number_of_commands = int(input())
while number_of_commands > 0:
    number_of_commands -= 1
    command = list(map(str, input().split()))
    if command[0] in "pop":
        s.pop()
    if command[0] in "remove":
        s.remove(int(command[1]))
    if command[0] in "discard":
        s.discard(int(command[1]))

print(sum(s))
