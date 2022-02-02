t = int(input())
cnt = 0

for i in range(t):
    connect = 1
    error = 0
    data = input()

    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            connect += 1
        elif data[i] != data[i+1]:
            if data.count(data[i]) > connect:
                error += 1
            connect  = 1
    
    if error == 0:
        cnt += 1
print(cnt)
