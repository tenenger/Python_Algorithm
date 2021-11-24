# n은 data 수, m은 더하는 총 횟수, k는 최대로 큰수를 더할 수 있는 횟수
# 합산을 구하시오
# n=6, m=8, k=3이고 [1,2,3,4,5,6]이라면, 6+6+6+5+6+6+6+5 = 46

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]
result = 0
while True :
    for _ in range(3) :
        if m == 0 :
            break
        result += first
        m -= 1
    if m == 0 :
        break
    result += second
    m -= 1
print(result)