data = input()
ucpc = ['U', 'C', 'P', 'C']
cnt = 0

for i in ucpc:
    if i in data:
        cnt += 1
        data = data[data.index(i) + 1:]
    else:
        print('I hate UCPC')
        break
if cnt == 4:
    print('I love UCPC')