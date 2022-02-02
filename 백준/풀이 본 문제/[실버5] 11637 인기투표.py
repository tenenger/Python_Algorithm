t = int(input())
for _ in range(t):
    n = int(input())
    data = [int(input()) for i in range(n)]
    if data.count(max(data)) != 1:
            print('no winner')
    else:
        if max(data) > sum(data)/2 :
            idx = data.index(max(data)) +1
            print(f'majority winner {idx}')
        else:
            idx = data.index(max(data)) +1
            print(f'minority winner {idx}')