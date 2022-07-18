def average(array):
    # your code goes here
    sum_of_distinct_heights = 0
    total_number_of_distinct_height = len(set(array))
    for i in set(array):
        sum_of_distinct_heights += i
    return sum_of_distinct_heights / total_number_of_distinct_height


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
