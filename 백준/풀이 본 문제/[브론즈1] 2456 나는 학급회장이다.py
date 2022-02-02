n = int(input())
cnt = [0]*3
data = [[0]*3 for _ in range(3)]

for _ in range(n):
    score = list(map(int,input().split()))
    
    for i in range(3):
        cnt[i] += score[i]
        data[i][score[i]-1] += 1

m = max(cnt)
ID = []
if cnt.count(m) == 1:
    print(cnt.index(m)+1, m)
else:
    ID = list(filter(lambda x: cnt[x] == m, range(len(cnt))))

    
    for j in range(2, -1, -1):
        arr = []
        for i in ID:
            arr.append(data[i][j])
        if arr.count(max(arr)) == 1:
            print(ID[arr.index(max(arr))]+1, m)
            break
        else:
            continue
    if j == 0 and arr.count(max(arr)) >= 2:
        print(0, m)


