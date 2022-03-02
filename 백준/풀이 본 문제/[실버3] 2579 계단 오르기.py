import sys
input = sys.stdin.readline
n = int(input())
stairs = [int(input()) for _ in range(n)] + [0] * 2
dp = [0] * (n + 2)
dp[0] = stairs[0]
dp[1] = sum(stairs[:2])
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

if n <= 2:
    print(dp[n-1])
else:
    for i in range(3, n):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
    print(dp[n-1])
