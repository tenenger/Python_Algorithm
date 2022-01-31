string = input()
alphabat = {}
for i in string:
    if i not in alphabat:
        alphabat[i] = 1
    else:
        alphabat[i] += 1

cnt = 0
middle = ''
error = False
for j in alphabat:
    if alphabat[j] % 2 == 1:
        middle = j
        cnt += 1
        if cnt >= 2:
            error = True

result = ''
for k in alphabat:
    result += k * (alphabat[k]//2)
change = sorted(result)
result = ''.join(change)
pelindrom = ''
pelindrom = result + middle + result[::-1]

if error:
    print("I'm Sorry Hansoo")
else:
    print(pelindrom)
