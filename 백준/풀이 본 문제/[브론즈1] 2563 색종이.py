t = int(input())
d = [[0]*100 for _ in range(100)]

for i in range(t):
    x,y=map(int,input().split())
    for j in range(y, y+10):
        for k in range(x, x+10):
            d[j][k] = 1
cnt = 0
for i in range(100):
    cnt += sum(d[i])
print(cnt)