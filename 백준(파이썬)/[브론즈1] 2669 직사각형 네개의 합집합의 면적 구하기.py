data = [[0]*100 for i in range(100)]
for i in range(4):
    a,b,c,d = map(int, input().split())
    
    for j in range(a,c):
        for k in range(b,d):
            data[j][k] = 1
result = 0
for i in data:
    result += sum(i)
print(result)