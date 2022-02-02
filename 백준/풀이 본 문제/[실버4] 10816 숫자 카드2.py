import sys
input = sys.stdin.readline
n = int(input())
card = map(int, input().split())
m = int(input())
search = map(int, input().split())
arr = [0]*20000000

for i in card:
    arr[i] += 1
for j in search:
    print(arr[j], end=" ")
