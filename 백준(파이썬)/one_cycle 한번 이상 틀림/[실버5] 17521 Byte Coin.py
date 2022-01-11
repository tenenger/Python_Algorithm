n, w = map(int, input().split())
data = [int(input()) for _ in range(n)] + [0]
coin = 0
for i in range(1, n+1):
    if data[i-1] < data[i] and not coin:
        coin = w // data[i-1]
        w = w % data[i-1]
    if data[i-1] > data[i]:
        w += coin * data[i-1]
        coin = 0
print(w)