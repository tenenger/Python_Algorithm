1번
n = int(input())
data = list(map(int, input().split()))
data.sort()
team = 0
count = 0

for i in data :
    count += 1
    if count == i :
        team += 1
        count = 0

print(team)
---------------------------------------------------------
2번 
data = input()
a = int(data[0])
for i in range(1, len(data)) :
    if a * int(data[i]) > a + int(data[i]) :
        a = a * int(data[i])
    else :
        a = a + int(data[i])
print(a)
----------------------------------------------------------
3번
data = input()
count_0 = 0
count_1 = 0

if data[0] == '0':
    count_0 += 1
if data[0] == '1':
    count_1 += 1

for i in range(len(data)-1) :
    if data[i] == data[i+1]:
        continue
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count_1 += 1
        if data[i+1] == '0' :
            count_0 += 1

if count_0 > count_1 :
    print(count_1)
else :
    print(count_0)
----------------------------------------------------------
4번 
n = int(input())
data = list(map(int, input().split()))
data.sort()
target = 1

for i in range(5) :
    if target < data[i]:
        break
    else :
        target += data[i]
print(target)
----------------------------------------------------------
5번. 1방법
n, m = map(int, input().split())
data = list(map(int, input().split()))
count = 0

for i in range(n) :
    for j in range(n) :
        if i != j and data[i] != data[j] :
            count += 1
        else :
            continue
print(count / 2)

5. 2방법
n, m = map(int, input().split())
data = list(map(int, input().split()))
weigh_list = [0]*11
count = 0

for i in data:
    weigh_list[i] += 1

for j in range(1, m+1):
    n = n - weigh_list[j]
    count += n * weigh_list[j]

print(count)

#------------------------------------------------------
6번 (모르겠어요, 다시 공부해서 풀어볼것!)
food_times = list(map(int, input().split()))
k = int(input())
second = 0
result = 0
food = len(food_times)

while True :
    for i in range(food) :
        if food_times == 0 :
            continue
        else :
            food_times[i] = food_times[i] - 1
            second += 1
            if second == k :
                result = i
                print(result)
                break
