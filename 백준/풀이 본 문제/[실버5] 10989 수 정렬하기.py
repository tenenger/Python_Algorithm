import sys

n = int(sys.stdin.readline())
# (n+1)말고 10001로해야 오류가 안나온다..?
# 계수정렬방법을 이용
d = [0] * (10001)

for _ in range(n):
    d[int(sys.stdin.readline())] += 1
    
for i in range(len(d)):
    for j in range(d[i]):
        print(i)