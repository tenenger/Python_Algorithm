t = int(input())
for _ in range(t) :
    h, w, n = map(int, input().split())
    high = n % h
    floor = n // h + 1
    if n % h == 0:
        high = h
        floor = n // h
    print(str(high)+'{:02d}'.format(floor))