n = int(input())
A = list(map(int, input().split()))
B = sorted(A)
result = []
for i in A:
    idx = B.index(i)
    B[idx] = '*'
    result.append(idx)
print(' '.join(map(str, result)))
