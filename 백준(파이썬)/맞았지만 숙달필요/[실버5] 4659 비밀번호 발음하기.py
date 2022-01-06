need = 'aeiou'

while True:
    right = 0
    arr_1 = []
    arr_2 = []
    password = input()
    if password == 'end':
        break
    for i in need:
        if i in password:
            right += 1
    if right == 0:
        print(f'<{password}> is not acceptable.')
        continue
    if len(password) == 1:
        print(f'<{password}> is acceptable.')
        continue
    if password[0] in need:
        arr_1.append(password[0])
    else:
        arr_2.append(password[0])
    for j in range(1, len(password)):
        if password[j] == password[j-1]:
            if password[j] in 'eo':
                pass
            else:
                print(f'<{password}> is not acceptable.')
                break
        if password[j] in need:
            arr_2 = []
            arr_1.append(password[j])
            if 'ee' in arr_1:
                arr_1.remove('ee')
            if 'oo' in arr_2:
                arr_1.remove('oo')
        elif password[j] not in need:
            arr_1 = []
            arr_2.append(password[j])
        if len(arr_2) == 3 or len(arr_1) == 3:
            print(f'<{password}> is not acceptable.')
            break
        if j == len(password)-1 and (len(arr_2) <= 2 or len(arr_1) <= 2):
            print(f'<{password}> is acceptable.')
            break
                
            

    