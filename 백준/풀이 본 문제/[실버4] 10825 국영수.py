import sys
input = sys.stdin.readline
n = int(input())
data = [input().split() for i in range(n)]
data.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for person in data:
    print(person[0])
