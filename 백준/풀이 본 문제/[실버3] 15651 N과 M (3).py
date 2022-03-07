from itertools import product
n, m = map(int, input().split())
result = list(product(range(1, n+1), repeat=m))
for permutation in result:
    print(" ".join(map(str, permutation)))
