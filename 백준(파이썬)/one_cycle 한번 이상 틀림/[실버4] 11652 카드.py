import sys
input = sys.stdin.readline
n = int(input())
dict = {}
for i in range(n):
    data = int(input())
    if data in dict:
        dict[data] += 1
    else:
        dict[data] = 1

result = sorted(dict.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])
