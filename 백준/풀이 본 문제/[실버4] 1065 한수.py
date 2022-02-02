def solution(num):
    if num <= 99:
        return num
    else:
        cnt = 99
        for i in range(100, num+1):
            arr = list(map(int, str(i)))
            if arr[0]-arr[1] == arr[1]-arr[2]:
                cnt += 1
        return cnt

num = int(input())
print(solution(num))