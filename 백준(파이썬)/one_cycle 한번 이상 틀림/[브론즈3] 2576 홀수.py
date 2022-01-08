data = [int(input()) for _ in range(7)]
a = []
for i in range(7) :
    if data[i] % 2 == 1 :
        a.append(data[i])
if not a :
    print(-1)
else :
    print(sum(a))
    print(min(a))