# Enter your code here. Read input from STDIN. Print output to STDOUT
count_number_of_elements_a = int(input())
number_of_elements_a = set(map(int, input().split()))
count_of_other_sets = int(input())

while count_of_other_sets > 0:
    count_of_other_sets -= 1
    operation = list(map(str, input().split()))
    new_set = set(map(int, input().split()))
    if operation[0] == "intersection_update":
        number_of_elements_a.intersection_update(new_set)
    if operation[0] == "update":
        number_of_elements_a.update(new_set)
    if operation[0] == "symmetric_difference_update":
        number_of_elements_a.symmetric_difference_update(new_set)
    if operation[0] == "difference_update":
        number_of_elements_a.difference_update(new_set)

print(sum(number_of_elements_a))