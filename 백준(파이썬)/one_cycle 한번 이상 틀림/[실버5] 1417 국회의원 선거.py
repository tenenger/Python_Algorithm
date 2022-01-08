n = int(input())
cnt = 0
data = [int(input()) for i in range(n)]
if n == 1:
    print(0)
else:
    maesu = data[1:]
    maesu.sort()
    while True:
        if data[0] > max(maesu):
            break
        else:
            idx = maesu.index(max(maesu))
            number = maesu.pop(idx)
            number -= 1
            maesu.append(number)
            cnt += 1
            data[0] += 1
    print(cnt)
