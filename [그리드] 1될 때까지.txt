'''
n = 1 될 때까지 
1. n - 1
2. n / 4
1번 2번을 반복하는 횟수를 구하시오
'''
n, k = map(int, input().split())
count = 0

while True :
    if n % k != 0 :
        n -= 1
        count += 1
    if n % k == 0 :
        n /= k
        count += 1
    if n == 1 :
        break
print(count)
