t = int(input())
error = 0
for _ in range(t):
    word = input()
    stack = []
    for alphabat in word:
        if stack:
            if stack[-1] == alphabat:
                stack.pop()
            else:
                stack.append(alphabat)
        else:
            stack.append(alphabat)
    if stack:
        error += 1
result = t - error
print(result)
# 왼쪽부터 알파벳을 세어, 같은 짝이 있으면 pop()하고, 아니면 더하여 stack에 알파벳이 있을경우 에러가 있고, 아니면 좋은 단어이다.
