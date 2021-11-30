data = [list(map(int, input().split())) for _ in range(5)]
result = 0
for i in range(5) :
    if result < sum(data[i]) :
        result = sum(data[i])
        count = i + 1
print(count, result)
