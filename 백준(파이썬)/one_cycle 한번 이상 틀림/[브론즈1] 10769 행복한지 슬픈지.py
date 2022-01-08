data = input()

cnt_sad = data.count(':-(')
cnt_smile = data.count(':-)')

if cnt_sad == cnt_smile == 0:
    print('none')
elif cnt_sad < cnt_smile:
    print('happy')
elif cnt_sad == cnt_smile:
    print('unsure')
elif cnt_sad > cnt_smile:
    print('sad')