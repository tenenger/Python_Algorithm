n = int(input())

data = [tuple(map(int, input().split())) for _ in range(n)]
score = []

for i in range(n):
    cnt = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            cnt += 1
    score.append(cnt + 1)
print(" ".join(map(str, score)))