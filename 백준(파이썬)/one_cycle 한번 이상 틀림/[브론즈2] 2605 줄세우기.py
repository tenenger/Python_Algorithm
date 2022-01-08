t = int(input())

data = list(map(int, input().split()))
d= [1]
for i in range(1, t):
    d.insert(data[i], i+1)

d.reverse()
print(" ".join(map(str, d)))