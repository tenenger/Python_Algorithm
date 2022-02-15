string = input()
stack = []
cnt = 0
for i in string:
    if i == '(':
        stack.append(i)
    else:
        if len(stack) == 0:
            cnt += 1
        else:
            stack.pop()
cnt += len(stack)
print(cnt)
