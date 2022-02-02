# 집합자료형은 특정 데이터가 존재하는지 검사하는데 아주 효과적이다.
# set()함수는 문자열, 리스트 등 {}형태로 바꾸어주는 함수이다.

n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x :
    if i in array :
        print("yes", end=" ")
    else :
        print("no", end=" ")
