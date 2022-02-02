from itertools import permutations
import copy
t = int(input())
data = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
result = copy.deepcopy(data)

for i in range(t):
    answer, strike, ball = map(int, input().split())
    answer = tuple(str(answer))
    remove_cnt = 0

    for j in range(len(result)):
        j -= remove_cnt
        strike_cnt, ball_cnt = 0, 0

        for k in range(3):
            if int(answer[k]) in result[j]:
                if k == result[j].index(int(answer[k])):
                    strike_cnt += 1
                else:
                    ball_cnt += 1
        if strike_cnt != strike or ball_cnt != ball:
            result.remove(result[j])
            remove_cnt += 1

print(len(result))
# 여기서 중요한 점은 삭제될때 리스트크기가 줄어드는것을 remove_cnt로 숫자를 세고, j -= remove_cnt함으로써 리스트가 줄어들때 이상한 것을 가져오는것을 막아준다. 꼭 중요하다.
