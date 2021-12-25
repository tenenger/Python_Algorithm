# n이 5보다 작을경우에 인덱스 에러가 발생한다.
# 그래서 n에 +5를 해준다.

n = int(input())
d= [100001]*(n+5)
d[2] = d[5] = 1
d[4] = 2

for i in range(6, n+5):
    d[i] = min(d[i-5], d[i-2]) + 1

if d[n] == 100001:
    print(-1)
else:
    print(d[n])