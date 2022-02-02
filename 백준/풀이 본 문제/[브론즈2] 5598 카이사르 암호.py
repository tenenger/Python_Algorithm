data = input()
d = []
for i in data:
    if ord(i) <= ord('C'):
        print((chr(ord(i)+(ord('X')-ord('A')))), end="")
    else:
        print((chr(ord(i)-3)), end="")
