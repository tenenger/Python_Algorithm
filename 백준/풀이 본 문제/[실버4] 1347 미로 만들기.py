n = int(input())
key_press = list(input())
x, y = 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 2
walk_location = [(0, 0)]
max_x, max_y = 0, 0
for key in key_press:
    if key == 'R':
        direction = (direction + 1) % 4
    elif key == 'L':
        if direction - 1 == -1:
            direction = 3
        else:
            direction -= 1
    else:
        x += dx[direction]
        y += dy[direction]

    walk_location.append((x, y))
walk_location = list(walk_location)

srt_walk_location_x = sorted(walk_location, key=lambda x: x[0])
srt_walk_location_y = sorted(walk_location, key=lambda x: x[1])
min_x, min_y = srt_walk_location_x[0][0], srt_walk_location_y[0][1]
x_size = srt_walk_location_x[-1][0] - srt_walk_location_x[0][0]
y_size = srt_walk_location_y[-1][1] - srt_walk_location_y[0][1]

box = [['#']*(x_size + 1) for _ in range(y_size + 1)]

for walk_x, walk_y in walk_location:
    box[walk_y + abs(min_y)][walk_x + abs(min_x)] = '.'

for result in box[::-1]:
    print(''.join(result))
