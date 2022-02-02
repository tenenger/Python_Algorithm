arr = [input() for _ in range(5)]
cnt = 0

for i in range(len(arr)):
    if cnt < len(arr[i]):
        cnt = len(arr[i])


for i in range(cnt):
    for j in range(5):
        if i > len(arr[j]) -1:
            continue
        else:
            print(arr[j][i], end="")