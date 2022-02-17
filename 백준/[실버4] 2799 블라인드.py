dic = {'................': 0,
       '****............': 0,
       '********........': 0,
       '************....': 0,
       '****************': 0}

m, n = map(int, input().split())
windows = [list(input()) for _ in range(5*m + 1)]
x, y = 1, 1
for i in range(m):
    a, b = x, y
    for j in range(n):
        window = []
        for k in range(4):
            for q in range(4):
                window.append(windows[a+k][b+q])
        dic[''.join(window)] += 1
        b += 5
    x += 5
for key, value in dic.items():
    print(value, end=' ')
