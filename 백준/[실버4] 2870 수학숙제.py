n = int(input())

arr = []
for _ in range(n):
    string = input()
    number = ''
    for i in range(len(string)):
        if string[i].isdigit():
            number += string[i]
        else:
            if number == '':
                continue
            else:
                arr.append(int(number))
                number = ''
        if number != '' and i == len(string)-1:
            arr.append(int(number))
            number = ''
arr.sort()
print('\n'.join(map(str, arr)))
