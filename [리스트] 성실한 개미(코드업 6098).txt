6098 [기초-리스트] 성실한 개미(py)

world_map = [list(map(int, input().split())) for _ in range(10)]
a, b = 2, 2

while True :
    world_map[a-1][b-1] = 9
    b += 1
    if world_map[a-1][b-1] == 0 :
        continue
    if world_map[a-1][b-1] == 1 :
        b -= 1
        a += 1
        if world_map[a-1][b-1] == 0 :
            continue
        if world_map[a-1][b-1] == 1 :
            a -= 1
            break
    if world_map[a-1][b-1] == 2 :
        world_map[a-1][b-1] = 9
        break
for i in range(10) :
    for j in range(10) :
        print(world_map[i][j], end=" ")
    print()