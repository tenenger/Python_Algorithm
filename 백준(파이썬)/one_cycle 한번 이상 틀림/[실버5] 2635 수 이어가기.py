n = int(input())
max_arr = []
max_cnt = 0
for i in range(n//2+1, n+1):
    arr = [n, i]
    while True:
        if arr[-2] - arr[-1] < 0:
            break
        next_num = arr[-2] - arr[-1]
        arr.append(next_num)
    if len(arr) > max_cnt:
        max_arr = arr
        max_cnt = len(arr)

print(max_cnt)
print(" ".join(map(str, max_arr)))


        