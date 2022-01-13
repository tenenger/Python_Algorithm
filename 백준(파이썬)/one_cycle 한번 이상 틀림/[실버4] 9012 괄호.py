n = int(input())
for i in range(n):
    data = input()
    cnt = 0
    if data.count('(') == data.count(')') :
        for j in data:
            if j == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                break
        if cnt == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')