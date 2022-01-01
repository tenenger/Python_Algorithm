t = int(input())
cow = [-1]*11
cnt = 0

for i in range(t):
    a, b = map(int, input().split())
    if cow[a] == -1:
        cow[a] = b
    else:
        if cow[a] != b:
            cnt += 1
            cow[a] = b
print(cnt)