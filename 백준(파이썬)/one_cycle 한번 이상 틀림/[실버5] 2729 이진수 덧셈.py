t = int(input())
for _ in range(t):
    a, b = input().split()
    a = int(a, 2)
    b = int(b, 2)
    result = a+b
    print(format(result, 'b'))
