n = int(input())

list_2017 = [0, 5000000, 3000000, 2000000, 500000, 300000, 100000]
list_2018 = [0, 5120000, 2560000, 1280000, 640000, 320000]

for i in range(n) :
    a, b = map(int, input().split())
    count = 0
    rank_2017 = 0
    rank_2018 = 0

    for k in range(1, 6+1) :
        if a == 0 :
            break
        rank_2017 += k
        if a <= rank_2017 :
            count += list_2017[k]
            break

    for j in range(1, 5+1) :
        if b == 0 :
            break
        rank_2018 += 2 ** (j-1)
        if b <= rank_2018 :
            count += list_2018[j]
            break

    print(count)
