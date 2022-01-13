n = int(input())
numbers = list(map(int, input().split()))
cnt = 0
for number in numbers:
    error = 0
    if number > 1:
        for i in range(2, number//2+1):
            if number % i == 0:
                error = 1
                break
        if error == 0:
            cnt += 1
print(cnt)
                
        