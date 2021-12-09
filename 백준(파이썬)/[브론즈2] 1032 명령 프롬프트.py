n = int(input())

data = [input() for i in range(n)]
first = list(data[0])

for i in range(1, n):
    for j in range(len(first)):
        if first[j] != data[i][j]:
            first[j] = '?'
print("".join(first))