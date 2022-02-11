import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    cnt = 0
    while n // 5 != 0:
        n = n // 5
        cnt += n
    print(cnt)
