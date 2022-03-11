from itertools import permutations
n, m = map(int, input().split())
data = list(sorted(map(int ,input().split())))
result = list(permutations(data, m))
for i in result:
    print(" ".join(map(str, i)))