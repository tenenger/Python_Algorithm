li = sorted([input()[0] for _ in range(int(input()))])
s = set(li)
res = []

for i in s:
    if li.count(i) >= 5:
       res.append(i)


if len(res) > 0:
    print("".join(sorted(res)))
else:
    print("PREDAJA")