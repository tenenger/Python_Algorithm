[구현] 왕실의 나이트

1. 내가 푼 방법

location = input()
move_x, mover_y = 0, 0
dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [-2, -2, -1, 1, 2, 2, 1, -1]
type = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
count = 0

for i in range(len(type)) :
    move_x = ord(location[0]) + dx[i]
    move_y = int(location[1]) + dy[i]
    if move_x >= 105 or move_x <= 96 or move_y >=9 or move_y <= 0:
        continue
    count += 1
print(count)

----------------------------------------------------------
2. 해답

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0

for step in steps :
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 or next_column >= 1 or next_row <= 8 or next_column <= 8 :
        result += 1
print(result)