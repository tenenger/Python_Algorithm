w, h = map(int, input().split())
x_list = [0, w]
y_list = [0, h]
n = int(input())
for i in range(n):
    cut_direction, idx = map(int, input().split())
    if cut_direction == 0:
        y_list.append(idx)
    else:
        x_list.append(idx)
    
x_list.sort()
y_list.sort()

max_size = 0

for i in range(1, len(x_list)):
    for j in range(1, len(y_list)):
        width = x_list[i] - x_list[i-1]
        height = y_list[j] - y_list[j-1]
        max_size = max(max_size, width * height)
print(max_size)