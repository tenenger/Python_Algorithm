n = int(input())
result = []

i = 2
while n != 1:
    
    if n % i == 0:
        result.append(str(i))
        n = n / i
        i == 2
    else:
        i += 1
print("\n".join(result))