number = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = 0
A.sort()
B.sort(reverse=True)
for i in range(number):
    result += A[i] * B[i]
print(result)
