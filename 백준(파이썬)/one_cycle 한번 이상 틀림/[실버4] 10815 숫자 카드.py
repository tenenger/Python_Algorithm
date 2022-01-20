import sys
input = sys.stdin.readline
n = int(input())
card = list(map(int, input().split()))
m = int(input())
search = list(map(int, input().split()))
card.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
    return 0


result = []
for i in search:
    result.append(binary_search(card, i, 0, len(card)-1))
print(' '.join(map(str, result)))
