t = int(input())
dp = [float(input()) for _ in range(t)]
for i in range(1, t):
    dp[i] = max(dp[i], dp[i-1] * dp[i])
print('{:.3f}'.format(max(dp)))
