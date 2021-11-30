n = int(input())
data = [float(input()) for _ in range(n)]

for i in range(n) :
    print('${:.2f}'.format(round(data[i]*0.8, 2)))