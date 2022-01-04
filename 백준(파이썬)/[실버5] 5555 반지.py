search = input()
n = int(input())
cnt = 0
for i in range(n):
    ring = input()
    for i in range(10):
        ring = ring[1:] + ring[0]
        if search in ring:
            cnt += 1
            break
print(cnt)
