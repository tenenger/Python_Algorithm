# 백준 14720
market 은 가게수
딸기, 바나나, 초코, 딸기, 바나나, 초코 ... 순으로 먹어야하는 규칙
0        1       2      0      1       2    ...
하나 먹을때 마다 count에 추가

market = int(input())
data = list(map(int, input().split()))
count = 0
current_milk = 0

for i in range(market) :
    if data[i] % 3 == current_milk % 3 :
        count += 1
        current_milk += 1
print(count)