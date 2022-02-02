string = input()
a = len(string)
result = []
for i in range(a-2):
    for j in range(i+1, a-1):
        for k in range(j+1, a):
            result.append(string[:j][::-1] + string[j:k][::-1] + string[k:][::-1])
print(min(result))

