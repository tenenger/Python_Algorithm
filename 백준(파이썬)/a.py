jeme = list(map(int, input().split()))
jurli = list(map(int, input().split()))
cnt_1 = 0
cnt_2 = 0
for i in range(9):
    cnt_1 += jeme[i]
    if cnt_1 > cnt_2:
        print('Yes')
        break
    cnt_2 += jurli[i]
    if i == 8:
        print('No')