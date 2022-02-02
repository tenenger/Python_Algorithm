n = int(input())
start = 0
end = 1
answer = 1
sum_number = 1

while start < n//2 +1:
    if sum_number < n:
        end += 1
        sum_number += end
    elif sum_number > n:
        sum_number -= start
        start += 1
    else:
        answer += 1
        end+= 1
        sum_number += end
print(answer)
    