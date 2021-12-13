n = int(input())

while True:
    flag = True
    for i in str(n):
        if i != '4' and i != '7':
            n -= 1
            flag = False
            break
    if flag == True:
        print(n)
        break



    