a = int(input())
b = input()
data='abcdefghijklmnopqrstuvwxyz'
result = 0

for i in range(a):
    result += (data.index(b[i])+1) * pow(31, i)
print(result%1234567891)