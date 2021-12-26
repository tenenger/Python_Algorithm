k = int(input())
for i in range(k):
    cnt = 0
    data = list(map(int, input().split()))
    n = data[0]
    data = data[1:]
    data.sort(reverse=True)
    print(f'Class {i+1}')

    for j in range(1, len(data)):
        cnt = max(data[j-1] - data[j], cnt)

    print(f'Max {max(data)}, Min {min(data)}, Largest gap {cnt}')