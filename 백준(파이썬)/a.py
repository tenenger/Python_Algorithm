n = int(input())
cnt = n // 3
cnt += n % 3
if cnt % 2 == 1:
    print('SK')
else:
    print('CY')