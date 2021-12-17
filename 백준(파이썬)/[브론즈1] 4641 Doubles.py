while True:
    data = list(map(int, input().split()))
    if data == [-1]:
        break
    cnt = 0
    for i in range(len(data)-1):
        if data[i] * 2 in data:
            cnt += 1
    print(cnt)
            