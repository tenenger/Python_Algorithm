import math
n = input()
d = [0] * 10

for i in n:
    if int(i) == 9:
        i = 6
    d[int(i)] += 1
d[6] = math.ceil(d[6]/2)
print(max(d))
