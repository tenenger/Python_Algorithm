n = int(input())
papers = [list(input().split()) for i in range(n)]
color = {'white':0, 'blue':0}

def color_cnt(x, y, n):
    standard_color = papers[x][y]

    for i in range(x):
        for j in range(y):
            if papers[i][j] != standard_color:
                color_cnt(x, y, n // 2)
                color_cnt(x, y + n // 2, n // 2)
                color_cnt(x + n // 2, y, n // 2)
                color_cnt(x + n // 2, y + n // 2, n // 2)
                return
    if standard_color == '0':
        color['white'] += 1
    else:
        color['blue'] += 1

color_cnt(0, 0, n)
print(color['white'], color['blue'], sep="\n")
