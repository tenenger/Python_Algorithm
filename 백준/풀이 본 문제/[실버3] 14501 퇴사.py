n = int(input())
dp = [0] * (n + 1)
timetable = [list(map(int, input().split())) for _ in range(n)]

for index in range(n-1, -1, -1):
    time = timetable[index][0]
    money = timetable[index][1]
    if index + time > n:
        dp[index] = dp[index+1]
    else:
        dp[index] = max(dp[index+1], money + dp[index + time])
print(dp[0])
