n = int(input())
words = [input() for _ in range(n)]
target = words[0]
target_length = len(target)
words.remove(target)

diction = {}
cnt = 0
for i in target:
    if i not in diction:
        diction[i] = 1
    else:
        diction[i] += 1

for word in words:
    check = {}
    error = 0
    for alphabat in word:
        if alphabat not in check:
            check[alphabat] = 1
        else:
            check[alphabat] += 1

    if diction == check:
        cnt += 1
    else:
        for key, value in diction.items():
            if key in check:
                check[key] -= value
            else:
                check[key] = -value
        result = list(check.values())
        error = sum(abs(number) for number in result)
        diff = abs(target_length - len(word))
        if diff <= 1 and error <= 2:
            cnt += 1
print(cnt)
