data = input()
stack = []
cnt = 0
for i in range(len(data)):
    if data[i] == '(':
        stack.append(i)
    elif data[i] == ')':
        if data[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else :
            cnt += 1
            stack.pop()
print(cnt)