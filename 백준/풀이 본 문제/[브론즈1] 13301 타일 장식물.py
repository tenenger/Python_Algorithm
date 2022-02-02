n =int(input())
d = [0] * 81
d[1], d[2] = 1, 1

for i in range(3, n+1):
    d[i] = d[i-2] + d[i-1]

def result(n):
    return d[n] * 4 + d[n-1] * 2
    
print(result(n))