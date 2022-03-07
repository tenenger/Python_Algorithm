k, n = map(int, input().split())
wires = [int(input()) for _ in range(k)]


def binary_search(arr, target, start, end):
    cut_list = []
    while start <= end:
        number = 0
        cut = (start + end) // 2

        for i in arr:
            number += i // cut
        if number >= target:
            cut_list.append(cut)
            start = cut + 1
        elif number < target:
            end = cut - 1
    return cut_list


result = binary_search(wires, n, 1, max(wires))
print(max(result))
