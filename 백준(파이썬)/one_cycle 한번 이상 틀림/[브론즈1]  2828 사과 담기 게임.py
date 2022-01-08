n, m = map(int, input().split())
j = int(input())
left = 1
right = m
cnt = 0

for i in range(j):
    apple_location = int(input())

    if right < apple_location:
        left += (apple_location - right)
        cnt += (apple_location - right)
        right = apple_location     

    elif apple_location <  left:
        right -= (left - apple_location)
        cnt += (left - apple_location)        
        left = apple_location

print(cnt)