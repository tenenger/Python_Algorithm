n = int(input())
if n % 8 == 1 :
    res = 1
elif n % 8 == 5 :
    res = 5
elif n % 4 == 3 :
    res = 3
else :
    a = n // 2
    if a % 4 == 2 or a % 4 == 3 :
        res = 4
    else :
        res = 2
print(res)