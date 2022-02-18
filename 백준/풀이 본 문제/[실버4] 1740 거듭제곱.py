n = int(input())
binary = format(n, 'b')
result = 0
number = 0
for i in binary[::-1]:
    tri = pow(3, number)
    result += tri * int(i)
    number += 1
print(result)
