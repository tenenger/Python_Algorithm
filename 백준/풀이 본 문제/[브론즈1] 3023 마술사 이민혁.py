n, m = map(int, input().split())
arr = [input() for _ in range(n)]
a,b = map(int, input().split())

for i in range(n):
    arr[i] += (arr[i])[::-1]

for j in range(n-1, -1, -1):
    arr.append(arr[j])

for cnt, k in enumerate(arr):
    if cnt == a-1:
        k = list(k)
        if k[b-1] == '.':
            k[b-1] = '#'
        else:
            k[b-1] = '.'
        print("".join(k))
    else:
        print(k)
