t = int(input())
dic = {
    'A+': 4.3,'A0': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
    'F': 0.0
}
data = [input().split() for i in range(t)]
cnt = 0
a = 0
for i in data:
    cnt += (int(i[1]) * dic[i[2]])
    a += int(i[1])

def my_round(a):
    # 만약 5이상이라면
    if a * 100 % 10 >=5:
        a = a + 0.001
    return round(a, 2)
    # 소수점 둘째자리까지 출력
print("{:.2f}".format(my_round(cnt/a)))
