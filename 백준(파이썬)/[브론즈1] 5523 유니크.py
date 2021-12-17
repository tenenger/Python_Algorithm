import copy
# 리스트 복사시에 deep카피를 사용해야 복사된 arr리스트의 값이 변경되어도 기존의 score리스트의 값이 안변한다. 꼭 기억하자.
n = int(input())
score = [list(map(int, input().split())) for i in range(n)]
arr = copy.deepcopy(score)

for i in range(3):
    for j in range(n):
        for k in range(j+1, n):
            if score[j][i] == score[k][i]:
                arr[k][i] = arr[j][i] = 0

for l in arr:
    print(sum(l))
