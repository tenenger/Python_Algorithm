d = {'.':46, 'O':79, '-':124, '|':45, '/':92, '\\':47,
'^':60, '<':118, 'v':62, '>':94}

n, m = map(int, input().split())
arr = [input() for i in range(n)]
rotate = []

for i in range(m-1, 0-1, -1):
    row = []
    for j in range(n):
        row.append('%c' % d[arr[j][i]])
    rotate.append(row)

for i in rotate:
    print("".join(i))
