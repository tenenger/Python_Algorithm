n = int(input())
dictionary = {}
for i in range(n):
    data = input()
    if data in dictionary:
        dictionary[data] += 1
    else:
        dictionary[data] = 1

result = sorted(dictionary.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])
