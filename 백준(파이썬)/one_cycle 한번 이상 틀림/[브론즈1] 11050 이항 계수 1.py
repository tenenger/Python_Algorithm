from itertools import combinations

n, k = map(int, input().split())

arr = [i for i in range(n)]

result = list(combinations(arr, k))

print(len(result))
