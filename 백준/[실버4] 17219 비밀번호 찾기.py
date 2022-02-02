import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
data = {}
for _ in range(n):
    site, pwd = input().strip().split()
    data[site] = pwd

for _ in range(m):
    search = input().strip()
    print(data[search])
