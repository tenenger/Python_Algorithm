[기초-리스트] 설탕과자 뽑기(py)

h, w = map(int, input().split())
paper = [[0]*w for i in range(h)]
n = int(input())
for i in range(n) :
    l, d, x, y = map(int, input().split())
    if d == 0 :
        for _ in range(l) :
            paper[x-1][y-1+_] = 1
    if d == 1 :
        for _ in range(l) :
            paper[x-1+_][y-1] = 1

for i in range(h) :
    for j in range(w):
        print(paper[i][j], end=" ")
    print()