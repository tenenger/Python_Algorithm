from itertools import permutations
n, m = map(int, input().split())
numbers = [x for x in range(1, n+1)]
result = list(permutations(numbers, m))
for i in result:
    print(" ".join(map(str, i)))
