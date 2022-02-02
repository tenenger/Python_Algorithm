x, y = [], []
for _ in range(3) :
    dx, dy = map(int, input().split())
    x.append(dx)
    y.append(dy)

for i in range(3) :
    if x.count(x[i]) == 1 :
        a = x[i]
    if y.count(y[i]) == 1 :
        b = y[i]
print(a, b)
