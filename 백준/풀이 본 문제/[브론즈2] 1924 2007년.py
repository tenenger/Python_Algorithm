a, b = map(int, input().split())
m = [31,28,31,30,31,30,31,31,30,31,30,31]
d = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

count = b
for i in range(a-1):
    count += m[i]

print(d[count % 7])