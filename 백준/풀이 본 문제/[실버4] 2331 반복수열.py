def solution(a):
    arr = [a]
    while True:
        cnt = 0
        for i in str(arr[-1]):
            cnt += pow(int(i), p)
        if arr.count(cnt) == 3:
            break
        arr.append(cnt)
    return arr


a, p = map(int, input().split())
result = solution(a)
remove_set = set()
for i in result:
    if result.count(i) >= 2:
        remove_set.add(i)
result = [i for i in result if i not in remove_set]
print(len(result))
# 중복값을 얻어 세트로 만들고, 컴프리헨션으로 중복되는 값은 전부 빼주었다.
