String = input()
data = [0,1,2,3]

for i in String :
    if i == 'A':
        data[1], data[2] = data[2], data[1]
    elif i == 'B' :
        data[2], data[3] = data[3], data[2]
    elif i == 'C':
        data[1], data[3] = data[3], data[1]
print(data.index(1))