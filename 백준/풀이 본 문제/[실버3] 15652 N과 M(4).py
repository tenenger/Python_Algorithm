from itertools import combinations_with_replacement
n, m = map(int, input().split())
result = list(combinations_with_replacement(range(1, n+1), repeat=m))
for permutation in result:
    print(" ".join(map(str, permutation)))
