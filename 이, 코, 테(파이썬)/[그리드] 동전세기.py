# [그리드] 동전세기

money = int(input())
count = 0
coin = [500, 100, 50, 10]

for i in coin :
    count += money // i
    money = money % i
print(count)