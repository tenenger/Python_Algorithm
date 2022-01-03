n, k = map(int, input().split())

def check(n, k):
    if n < k*(k+1) // 2:
        return -1
    if (n - (k*(k+1)/2)) % k == 0:
        return k-1
    else:
        return k
print(check(n,k))

