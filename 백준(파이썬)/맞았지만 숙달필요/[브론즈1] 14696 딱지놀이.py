t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(4,0,-1):
        if a[1:].count(i) > b[1:].count(i):
            print('A')
            break
        elif a[1:].count(i) < b[1:].count(i):
            print('B')
            break
        else:
            if i == 1:
                print('D')
            else:
                continue
    