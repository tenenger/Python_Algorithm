c = int(input())

for i in range(c):
    data = list(map(int, input().split() ))
    avg = sum(data[1:])/data[0]
    count = 0
    for j in range(1, data[0]+1):
        if data[j] > avg:
            count += 1
    print("{:.3f}%".format(count/data[0]*100))