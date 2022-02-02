t = int(input())
for i in range(t) :
    count = 0
    sum = 0
    n = int(input())
    for j in range(n) :
        a, b = map(float, input().split())
        count += a
        sum += a * b
    avg = sum / count
    print("{} {:.1f}".format(int(count), avg))