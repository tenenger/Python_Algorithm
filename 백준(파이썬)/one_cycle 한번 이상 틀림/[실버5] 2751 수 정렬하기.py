def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    d = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            d.append(left[i])
            i += 1
        else:
            d.append(right[j])
            j += 1
    if i != len(left):
        d += left[i:]
    
    if j != len(right):
        d += right[j:]
    return d
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
result = merge_sort(arr)
print("\n".join(map(str, result)))
