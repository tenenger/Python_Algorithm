n, m = map(int, input().split())
world_map = [ list(map(int, input())) for i in range(n) ]
print(world_map)
def dfs(x, y) :
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
    if world_map[x][y] == 0 :
        world_map[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

result = 0
for i in range(n) :
    for j in range(m) :
        if dfs(i, j) == True :
            result += 1
print(result)