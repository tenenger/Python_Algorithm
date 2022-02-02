n, m = map(int, input().split())
six, one = [], []
for _ in range(m):
    a, b = map(int, input().split())
    six.append(a)
    one.append(b)

if min(six) > min(one) * 6:
    result = n * min(one)
else:
    six_cnt = n // 6
    one_cnt = n % 6
    if min(six) > one_cnt * min(one):
        result = six_cnt * min(six) + min(one) * one_cnt
    else:
        result = (six_cnt+1) * min(six)
print(result)
