# 배열을 모든 수를 담을 수 있는 만큼 리스트를 만든다.

n = int(input())
array = [0] * 1000001

for i in input().split() :
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x :
    if array[i] == 1 :
        print("yes", end=" ")
    else :
        print("no", end=" ")
