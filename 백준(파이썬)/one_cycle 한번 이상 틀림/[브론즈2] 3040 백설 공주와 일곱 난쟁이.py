data = []

for i in range(9):
    data.append(int(input()))

cal = sum(data) -100

for i in range(len(data)-1):
    for j in range(i+1, len(data)):
        if data[i]+data[j] == cal:
            data.remove(data[i])
            data.remove(data[j-1])
            break
    if len(data) == 7:
        break

print("\n".join(map(str, data)))