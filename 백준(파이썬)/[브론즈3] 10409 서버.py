n, t= map(int, input().split())
data = list(map(int, input().split()))
sum = 0
count = 0
for i in range(n) :
    sum += data[i]
    if t < sum :
        print(i)
        break
    elif i == n-1:
        print(i+1)