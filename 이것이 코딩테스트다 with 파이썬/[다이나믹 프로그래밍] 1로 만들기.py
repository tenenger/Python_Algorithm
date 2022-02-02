x = int(input())
d = [0] * 30001                     # d 안에있는 값은 변환 횟수이다.

for i in range(2, x+1):             # 밑의 for 반복문은 횟수를 구하는 식이라고 보면 이해가능하다
    if i % 2 == 0 :
        d[i] = d[i//2] +1
    elif i % 3 == 0 :
        d[i] = d[i//3] +1
    elif i % 5 == 0 :
        d[i] = d[i//5] +1
    else :
        d[i] = d[i-1] +1


print(d[x])