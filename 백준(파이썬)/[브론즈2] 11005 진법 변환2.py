n, b = map(int, input().split())
result = []
B = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while n != 0:
    result.append(n % b)
    n = n // b
if not result :
    result.append(0)
while result:
    print(B[result.pop()], end="")