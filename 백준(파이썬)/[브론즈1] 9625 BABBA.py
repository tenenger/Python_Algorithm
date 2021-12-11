n = int(input())
a = [0]*46
b = [0]*46
a[0],a[1],a[2] = 1, 0, 1
b[0],b[1],b[2] = 0, 1, 1
for i in range(3, n+1):
    a[i] = a[i-2] + a[i-1]
    b[i] = b[i-2] + b[i-1]
print(a[n], b[n])