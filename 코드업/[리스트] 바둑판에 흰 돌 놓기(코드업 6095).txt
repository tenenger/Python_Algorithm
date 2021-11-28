답
zero = [[0]*19 for _ in range(19)]
n = int(input())

for i in range(n) :
    a, b = map(int, input().split())
    zero[a-1][b-1] = 1

for i in range(19) :
    for j in range(19) :
        print(zero[i][j], end=" ")
    print()

------------------------------------------------------------
답 아닌거 1
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
maps = [[0 for j in range(20)] for i in range(20)]

for l in range(n):
    for m in range(2) :
        maps[data[l][m]-1][data[l][m]-1] = 1

for _ in range(20):
    map_1 = []
    map_1 += map(str, maps[_])
    print(" ".join(map_1))
-------------------------------------------------------------
답 아닌거2
코드 업 [기초-리스트] 바둑판에 흰 돌 놓기

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
map = [[0 for j in range(20)] for i in range(20)]

for l in range(n):
    for m in range(2) :
        map[data[l][m]-1][data[l][m]-1] = 1
for k in range(20):
    print(map[k])
