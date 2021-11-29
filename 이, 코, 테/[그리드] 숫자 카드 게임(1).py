'''
숫자 카드 게임
첫줄 입력은 각 행, 열을 뜻한다.
3 3
각 행에 있는 가장 작은 숫자가 다른 행에 있는 작은 숫자보다 높은 숫자는 몇일까?
2 2 2
3 3 3
4 4 4
''' 
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(0, min_value)
print(result)