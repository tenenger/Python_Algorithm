while True:
    stack = []
    error = 0
    string = input()
    if string == '.':
        break
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                error = 1
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                error = 1
                break
    if error == 1 or stack:
        print('no')
    else:
        print('yes')
