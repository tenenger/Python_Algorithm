n = int(input())
data = list(map(int, input().split()))
data.insert(0, 0)
d = [0] * 100               # 최대값 저장장소
d[1] = data[1]              # 첫번째 값 입력
d[2] = max(d[1], data[2])  # 창고 2길이에서 창고 1에서 얻은 값이랑 창고 2에서 얻은 값 비교하여 큰거 입력

for i in range(3, n+1) :
    d[i] = max(d[i-1], d[i-2] + data[i])

print(d[n])