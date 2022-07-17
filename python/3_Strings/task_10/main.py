def print_rangoli(size):
    # your code goes here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    empty_list = []

    for i in range(0, size):
        if i == 0:
            length = len("-".join(alphabet[i + 1:size][::-1] + alphabet[i:size]))
        lst = "-".join(alphabet[i + 1:size][::-1] + alphabet[i:size]).center(length, "-")
        empty_list.append(lst)

    return print("\n".join(list(reversed(empty_list))[:-1] + empty_list))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

