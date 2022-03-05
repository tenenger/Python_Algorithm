n, m = map(int, input().split())
woods = list(map(int, input().split()))


def binary_search(array, target, start, end):
    cut_list = []
    while start <= end:
        result = 0
        cut = (start + end) // 2

        for wood in array:
            if wood - cut > 0:
                result += wood - cut
        if result >= target:
            cut_list.append(cut)
            start = cut + 1
        elif result < target:
            end = cut - 1
    return cut_list


print(max(binary_search(woods, m, 0, max(woods))))
