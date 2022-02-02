n = int(input())
data = list(map(int, input().split()))
students = int(input())
cnt = 1
for _ in range(students):
    gender, switch = map(int, input().split())
    if gender == 1:
        for i in range(switch, n+1, switch):
            data[i-1] = int(not data[i-1])
    else:
        mid = switch-1
        data[mid] = int(not data[mid])
        left = mid-1
        right = mid+1
        while True:

            if left <= -1 or right >= n:
                break
            if data[left] == data[right]:
                data[left] = int(not data[left])
                data[right] = int(not data[right])
                left -= 1
                right += 1
            else:
                break

for i in range(0, n, 20):
    print(' '.join(map(str, data[i:i+20])))
