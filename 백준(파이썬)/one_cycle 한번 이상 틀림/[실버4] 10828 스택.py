import sys
n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    data = sys.stdin.readline().split()
    if len(data) == 2:
        arr.append(int(data[1]))
    else:
        if data[0] == 'top':
            if len(arr) == 0:
                print(-1)
            else:
                print(arr[-1])
        elif data[0] == 'size':
            print(len(arr))
        elif data[0] == 'pop':
            if arr:
                print(arr.pop())
            else:
                print(-1)
        elif data[0] == 'empty':
            if arr :
                print(0)
            else:
                print(1)