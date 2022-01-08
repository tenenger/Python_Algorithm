n = int(input())
arr = []
for i in range(n):
    data = list(map(int, input().split()))
    cnt = 0
    for j in range(3):
        for k in range(j+1, 4):
            for q in range(k+1, 5):
                sum = (data[j] + data[k] + data[q])%10
                if cnt < sum :
                    cnt = sum
    arr.append(cnt)
win = list(filter(lambda x: arr[x] == max(arr), range(len(arr)) ))
print(max(win)+1)
    
