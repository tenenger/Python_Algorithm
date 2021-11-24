# 백준 2720 : 그리드 알고리즘

25, 10, 5, 1센트로 거스름돈 주기
t = 테스트 케이스 개수
data = 거슬러 줘야할 총 돈
count = coin 각 센트별 개수

t = int(input())
data = [int(input()) for _ in range(t)]
coin = [25, 10, 5, 1]
count = [0, 0, 0, 0]

for i in data :
    for j in range(len(coin)) :
        count[j] = i // coin[j]
        i = i % coin[j]
    print("{} {} {} {}".format(count[0], count[1], count[2], count[3]))