t = int(input())

sum = 0
for i in range(t) :
    count = 0
    data = input()

    for i in range(len(data)) :
        while data[i] == 'O' :
            count += 1
            i = i -1
            if i < 0 :
                break
    print(count)
