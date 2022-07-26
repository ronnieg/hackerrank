# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
number_of_rooms = list(map(int, input().split()))
number_of_rooms.sort()
print((set(number_of_rooms[0::2])^set(number_of_rooms[1::2])).pop())