array = [list(input()) for i in range(8)]

count = 0

for i in range(0, 7+1, 2):
    for j in range(0, 7+1, 2):
        if 'F' == array[i][j]:
            count += 1
        if 'F' == array[i+1][j+1]:
            count += 1

print(count)