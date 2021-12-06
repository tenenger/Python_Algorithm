n = list(input())
d = [0]*(len(n))

for i in range(len(n)):
    if i == 0:
        d[i] += 10
    elif n[i] == n[i-1]:
        d[i] += 5
    else: 
        d[i] += 10

print(sum(d))