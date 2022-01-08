r, c, zr, zc = map(int, input().split())
data = [list(input()) for i in range(r)]
arr = []
result = []

for k in data:
    for l in range(zr):
        arr.append(k)

for i in arr:
    row = []
    for j in i:
        row.append(j*zc)
    result.append(row)

for q in result:
    print("".join(q))