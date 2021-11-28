# 럭키 스트레이트 7번문제

n = input()
a = len(n)/2

left_num = list(map(int, n[:int(a)]))
right_num = list(map(int, n[int(a):]))

if sum(left_num) == sum(right_num):
    print("LUCKY")
else :
    print("READY")
---------------------------------------
# 문자열 재정렬 8번문제

data = input()
count = 0
list_data = []

for i in data :
    if i.isalpha():
        list_data.append(i)
    else :
        count += int(i)

list_data.sort()

if count != 0 :
    list_data.append(str(count))

print("".join(list_data))
--------------------------------------
