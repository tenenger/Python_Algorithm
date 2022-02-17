n, m = map(int, input().split())
cnt = 0
tiles = [list(input()) for _ in range(n)]
mid_line_tiles = ''
Vertical_line_tiles = ''

for i in range(n):
    for j in range(m):
        if tiles[i][j] == '-':
            mid_line_tiles += tiles[i][j]

        else:
            if len(mid_line_tiles) >= 1:
                cnt += 1
                mid_line_tiles = ''

    if len(mid_line_tiles) >= 1:
        cnt += 1
        mid_line_tiles = ''

for i in range(m):
    for j in range(n):
        if tiles[j][i] == '|':
            Vertical_line_tiles += tiles[j][i]

        else:
            if len(Vertical_line_tiles) >= 1:
                cnt += 1
                Vertical_line_tiles = ''
    if len(Vertical_line_tiles) >= 1:
        cnt += 1
        Vertical_line_tiles = ''

print(cnt)
