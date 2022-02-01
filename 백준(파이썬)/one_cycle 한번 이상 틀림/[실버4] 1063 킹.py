king, stone, num = input().split()
king_x, king_y = ord(king[0])-65, int(king[1])-1  # A1이면 0,0이다.
stone_x, stone_y = ord(stone[0])-65, int(stone[1])-1
move_direction = {'R': [1, 0],
                  'L': [-1, 0],
                  'B': [0, -1],
                  'T': [0, 1],
                  'RT': [1, 1],
                  'LT': [-1, 1],
                  'RB': [1, -1],
                  'LB': [-1, -1]
                  }

for i in range(int(num)):
    data = input()
    dx, dy = move_direction[data]
    if dx + king_x > 7 or dx + king_x < 0 or dy + king_y > 7 or dy + king_y < 0:
        continue  # 만약 king의 위치를 이동이 불가능할경우 이동명령을 무시한다.

    else:  # king의 이동이 가능하고,
        if king_x + dx == stone_x and king_y + dy == stone_y:  # king을 이동시켰을때 돌과 위치가 같고,
            if dx + stone_x > 7 or dx + stone_x < 0 or dy + stone_y > 7 or dy + stone_y < 0:
                # king과 돌의 위치가 같아 돌을 이동시키려고 했을때, 돌이 이동불가하면 이동명령을 무시한다.
                continue
            else:
                # king과 돌의 위치가 같아 돌을 이동시키려고 했을때, 돌이 이동가능하면 돌의 위치를 옮긴다.
                stone_x += dx
                stone_y += dy
        # king의 이동이 가능하면 이동시킨다.
        king_x += dx
        king_y += dy

king = str(chr(king_x + 65)) + str(king_y+1)
stone = str(chr(stone_x + 65)) + str(stone_y+1)
print(king, stone, sep='\n')
