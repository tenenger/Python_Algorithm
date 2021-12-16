s = input()
n = len(s)
r, c = 1, 1

for i in range(1, n+1):
    if n % i == 0 and i <= int(n / i):
        r = i
        c = int(n / i)
arr = [['']*c for _ in range(r)]
k = 0
for l in range(c):
    for j in range(r):
        arr[j][l] = s[k]
        k += 1

for i in arr:
    print("".join(i), end="")





