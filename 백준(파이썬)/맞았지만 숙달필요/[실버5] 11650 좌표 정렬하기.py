n = int(input())
data = [list(map(int, input().split())) for i in range(n)]
print(data)
# x는 data의 요소를 뜻하는거 같다.
data.sort(key= lambda x : (x[0], x[1]))
for i in data:
    print(" ".join(map(str, i)))