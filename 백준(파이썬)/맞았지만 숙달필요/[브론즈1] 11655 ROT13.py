a = input()

result = []
for i in a:
    if ord(i) + 13 > 90 and i.isupper():
        print(chr(ord(i)+ 13 - 26), end="")
    elif i.isspace() or i.isdigit():
        print(i, end="")
    elif ord(i) + 13 > 122 and i.islower():
        print(chr(ord(i)+ 13 - 26), end="")
    else:
        print(chr(ord(i) + 13), end="")
