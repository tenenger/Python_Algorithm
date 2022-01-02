n, l = map(int, input().split())
data = list(map(int, input().split()))

while data:
    if l >= min(data):
        l += 1
        data.remove(min(data))
    else:
        break
print(l)