s = input()
a = s.split('0')
b = s.split('1')

cnt_1, cnt_0 = 0, 0

for i in a:
    if i:
        cnt_1 += 1
for j in b:
    if j:
        cnt_0 += 1
print(min(cnt_1, cnt_0))