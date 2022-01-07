t = int(input())
for i in range(t):
    error = 0
    m = input()
    n = set(m)
    for j in n:
        if (m.count(j) +1) % 4== 0:
            error += 1
    if error == 0:
        print('OK')
    else:
        print('FAKE')