def solution(number):
    cnt = 0
    for i in range(len(number)-1):
        result_a, result_b = 1, 1
        for j in number[:i+1]:
            result_a *= int(j)
        for k in number[i+1:]:
            result_b *= int(k)
        if result_a == result_b:
            cnt += 1
    if cnt >= 1:
        return 'YES'
    return 'NO'

number = input()
print(solution(number))