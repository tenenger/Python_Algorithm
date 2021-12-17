n = int(input())

pic = [list(input()) for _ in range(n)]
k = int(input())

if k == 1:
    for i in pic:
        print("".join(i))
elif k == 2:
    arr= []
    for i in pic:
        arr.append(list(reversed(i)))
    for j in arr:
        print("".join(j))
else:
    pic.reverse()
    for i in pic:
        print("".join(i))
