n = int(input())
a = n//2
b = n//2
if n == 1 :
    a = 1
elif n % 2 == 1 :
    a += 1
print((a+1)*(b+1))