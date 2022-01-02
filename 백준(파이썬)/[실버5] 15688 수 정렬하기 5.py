import sys
input = sys.stdin.readline

n = int(input())
data = [int(input()) for i in range(n)]
data.sort()
print("\n".join(map(str, data)))