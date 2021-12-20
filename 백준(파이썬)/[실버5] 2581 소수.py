m = int(input())
n = int(input())
arr = []


for i in range(m, n+1):
    error = 0
    for j in range(1, i+1):
        if i % j == 0:
            error += 1
    if error == 2:
        arr.append(i)
if not arr:
    print('-1')
else:
    print(sum(arr), min(arr), sep="\n")
    
