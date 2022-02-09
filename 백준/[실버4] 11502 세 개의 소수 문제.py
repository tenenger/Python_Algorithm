t = int(input())

d = [True] * (1001)
d[0], d[1] = False, False
result = []
for i in range(2, 1001):
    if d[i]:
        result.append(i)
        for j in range(2, 1001):
            if i*j > 1000:
                break
            d[i*j] = False


def solution(arr, n):
    for i in arr:
        for j in arr:
            for k in arr:
                if i + j + k == n:
                    return ' '.join(map(str, sorted([i, j, k])))
    return 0


for _ in range(t):
    n = int(input())
    if n <= 5:
        print(0)
    else:
        arr = filter(lambda x: x < n, result)
        print(solution(result, n))
