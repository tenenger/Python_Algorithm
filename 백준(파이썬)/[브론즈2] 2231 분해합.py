num = int(input())
result = 0
for i in range(1, num+1):
    result = sum(map(int, str(i)))
    if num == result + i:
        print(i)
        break
    if i == num:
        print(0)