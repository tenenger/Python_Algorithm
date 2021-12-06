a = int(input())
b = int(input())
count = 0
rest = a % 100
a -= rest

while True:
    if count == 100:
        count = 0
        break
    if a % b == 0:
        break
    else:
        count += 1
        a += 1
        continue
print("{:02d}".format(count))