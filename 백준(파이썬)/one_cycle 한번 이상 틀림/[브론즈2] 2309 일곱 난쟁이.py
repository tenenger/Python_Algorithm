data = []
a, b = 0, 0
for i in range(9):
    data.append(int(input()))

for i in range(9):
    for j in range(i+1, 9):
        if sum(data) - (data[i] + data[j]) == 100 :
            a = data[i]
            b = data[j]

data.remove(a)
data.remove(b)

data.sort()
print('\n'.join(map(str, data)))