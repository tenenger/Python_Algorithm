ok = ["pi", "ka", "chu"]
speak = input()

for i in ok:
    speak = speak.replace(i, '*')
speak = speak.replace('*', '')
if speak:
    print('NO')
else:
    print('YES')