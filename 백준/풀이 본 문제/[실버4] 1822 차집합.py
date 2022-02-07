import sys
input = sys.stdin.readline
a, b = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))
result = a_set - b_set
result = sorted(result)
if result:
    print(len(result))
    print(' '.join(map(str, result)))
else:
    print('0')
