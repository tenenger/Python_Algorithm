import sys
m = int(sys.stdin.readline())
s = 0
for _ in range(m):
    data = sys.stdin.readline().split()
    if data[0] == 'all':
        s = (1 << 21) -1
    elif data[0] == 'empty':
        s = 0
    else:
        a, b = data[0], int(data[1])
        if a == 'add':
            s |= (1 << b)
        elif a == 'remove':
            s &= ~(1<<b)
        elif a == 'check':
            if s & (1<<b) == 0:
                print(0)
            else:
                print(1)
        else:
            s = s ^ (1 << b)