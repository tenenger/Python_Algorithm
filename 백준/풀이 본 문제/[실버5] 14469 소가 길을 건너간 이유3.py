n= int(input())
cnt = 0
data = [list(map(int, input().split())) for i in range(n)]
data.sort(key=lambda x: x[0])

for i in data:
    if cnt < i[0]:
        cnt = i[0]
        cnt += i[1]
    else:
        cnt += i[1]
print(cnt)