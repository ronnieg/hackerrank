# Enter your code here. Read input from STDIN. Print output to STDOUT
english_num = int(input())
english = set(map(int, input().split()))
french_num = int(input())
french = set(map(int, input().split()))
print(len(english.difference(french)))