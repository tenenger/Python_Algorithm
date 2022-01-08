l = int(input())
n = int(input())
d = [0] * l
real = 0
r_cnt = 0
r_number = 0

expect = 0
e_cnt = 0
e_number = 0


for i in range(1, n+1):
    p, k = map(int, input().split())
    for j in range(p-1, k):
        if d[j] != 0:
            continue
        else:
            d[j] = i
    e_cnt = k - p
    if e_cnt > expect:
        expect = e_cnt
        e_number = i

for j in range(1, n+1):
    r_cnt = d.count(j)
    if real < r_cnt:
        real = r_cnt
        r_number = j

print(e_number, r_number, sep="\n")