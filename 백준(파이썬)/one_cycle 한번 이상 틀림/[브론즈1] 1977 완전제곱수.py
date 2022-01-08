n = int(input())
m = int(input())
d = [i*i for i in range(1, int(m**0.5)+1)]
result =[]

for j in range(len(d)):
    if n<= d[j] <=m:
        result.append(d[j])
    elif d[j] > m:
        break

print(sum(result), min(result), sep="\n") if result else print(-1)
