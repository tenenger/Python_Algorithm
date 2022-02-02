import sys
input = sys.stdin.readline


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
    return 0


t = int(input())
for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()
    m = int(input())
    answer = list(map(int, input().split()))

    for j in answer:
        result = binary_search(data, j, 0, len(data)-1)
        print(result)
