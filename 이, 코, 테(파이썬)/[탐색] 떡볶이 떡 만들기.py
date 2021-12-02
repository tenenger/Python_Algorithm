# 재귀함수

n, m = map(int, input().split())
data = list(map(int, input().split()))

def binary_search(array, target, start, end) :
    while start <= end :
        sum = 0
        mid = (start+end) // 2
        for i in range(n) :
            if data[i] - mid < 0 :
                continue
            else :
                sum += data[i] - mid
        if sum == target :
            return mid
        elif sum > target :
            start = mid +1
        else :
            end = mid -1
    return None

result = binary_search(data, m, 0, max(data))
if result == None :
    print("없습니다.")
else :
    print(result)

    # 반복문사용

    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    start = 0
    end = max(array)

    result = 0
    while start <= end :
        total = 0
        mid = (start + end) // 2
        for x in array :
            if x - mid > 0 :
                total += x - mid
        if total < m :
            end = mid -1
        else :
            result = mid
            start = mid +1
print(result)