n = int(input())
t = [0]*36
t[0] = 1

for i in range(1, n+1):
    sum = 0
    for j in range(i):
        sum += t[j] * t[i-j-1]
    t[i] = sum
print(t[n])
