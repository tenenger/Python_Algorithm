n = int(input())
datas = [input() for _ in range(n)]
k = -1

while True:
    result = []
    for data in datas:
        result.append(data[k:])
    if len(result) == len(set(result)):
        break
    k -= 1
print(abs(k))
