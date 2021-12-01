n = int(input())

while 1 :
    num = int(input())
    if num == 0 :
        break

    elif num % n == 0 :
        print('{} is a multiple of {}.'.format(num, n))
    else :
        print('{} is not a multiple of {}.'.format(num, n))