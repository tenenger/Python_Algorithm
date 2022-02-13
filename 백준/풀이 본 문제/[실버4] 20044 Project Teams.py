n = int(input())
data = list(map(int, input().split()))
data.sort()
left = 0
right = len(data) - 1
min_value = 1e7
while left < right:
    min_value = min(min_value, data[left] + data[right])
    left += 1
    right -= 1
print(min_value)
