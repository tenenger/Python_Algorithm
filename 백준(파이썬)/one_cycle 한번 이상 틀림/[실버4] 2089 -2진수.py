import math
n = int(input())
if n == 0:
    print(0)
result = ''
while n:
    remain = n % -2
    quitient = math.ceil(n/-2)
    if remain < 0:
        remain *= (-1)

    n = quitient
    result = str(remain) + result
print(result)
