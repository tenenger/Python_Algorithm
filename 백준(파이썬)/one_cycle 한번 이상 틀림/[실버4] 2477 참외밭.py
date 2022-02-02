n = int(input())
box = [list(map(int, input().split())) for _ in range(6)]
max_width, max_height = 0, 0
min_width, min_height = 0, 0

for i in range(len(box)):
    if box[i][0] == 1 or box[i][0] == 2:
        height = box[i][1]
        if max_height < height:
            max_height = height
            max_height_idx = i

    elif box[i][0] == 3 or box[i][0] == 4:
        width = box[i][1]
        if max_width < width:
            max_width = width
            max_width_idx = i

min_width_idx = (max_width_idx+3) % 6
min_height_idx = (max_height_idx+3) % 6
min_width = box[min_width_idx][1]
min_height = box[min_height_idx][1]

result = n * ((max_height * max_width) - (min_width * min_height))
print(result)
