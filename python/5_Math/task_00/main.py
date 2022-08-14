# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


AB = int(input())
BC = int(input())

AC = math.sqrt(pow(AB, 2) + pow(BC, 2))
angle = round(math.degrees(math.acos(BC/AC)))
print(angle, chr(176), sep="")



