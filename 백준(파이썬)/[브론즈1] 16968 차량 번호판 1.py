d = {'c':26, 'd':10}
data = input()

result = d[data[0]]

for i in range(1, len(data)):
    mul = d[data[i]]
    if data[i] == data[i-1]:
        mul -= 1
    result *= mul
print(result)