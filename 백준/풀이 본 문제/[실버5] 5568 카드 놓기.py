from itertools import permutations
n = int(input())
k = int(input())
data = [input() for i in range(n)]
result = set()

for arr in permutations(data, k):
    result.add("".join(arr))

print(len(result))