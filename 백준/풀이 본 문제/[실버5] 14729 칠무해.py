import sys
input = sys.stdin.readline
n = int(input())
data = [float(input()) for _ in range(n)]
data.sort()
    
for i in range(7):
    print('{:.3f}'.format(data[i]))