n, l = map(int, input().split())
time = 0
location = 0
for _ in range(n):
    d, r, g = map(int, input().split())
    time += (d - location)
    if time % (r + g) < r:
        time += (r - (time % (r + g)))
    location = d
time += (l-location)
print(time)
