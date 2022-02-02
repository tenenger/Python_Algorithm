data = [int(input()) for _ in range(8)]

mx_score = []
mx_li = []

for _ in range(5):
    mx_li.append(data.index(max(data))+1)
    mx_score.append(max(data))
    data[data.index(max(data))] = -1

mx_li.sort()

print(sum(mx_score))
print(" ".join(map(str, mx_li)))