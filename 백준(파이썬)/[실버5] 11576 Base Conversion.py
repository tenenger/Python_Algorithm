a, b = map(int, input().split())
n = int(input())
data = list(map(int, input().split()))
data.reverse()
cnt = 0

for i in range(n):
    cnt += data[i] * pow(a, i)

result = []
while True:
    result.append(cnt % b)
    cnt = cnt // b
    if cnt >= b:
        continue
    else:
        result.append(cnt)
        break
result.reverse()
print(" ".join(map(str, result)))