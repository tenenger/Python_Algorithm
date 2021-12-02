t = int(input())

for i in range(t) :
    data = list(map(int, input().split()))
    s = [data[i]+data[i+4] for i in range(4)]
    print(max(s[0], 1) + max(s[1], 1) * 5 + max(s[2], 0) * 2 + s[3] * 2)