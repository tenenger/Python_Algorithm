n = int(input())
all_data = list(map(int, input().split()))
m = int(input())
m_data = list(map(int, input().split()))

all_data.sort()

def binary_search(array, target, start, end) :
    while start <= end :
        mid = (start+end)//2
        if target < all_data[mid] :
            end = mid -1
        elif target == all_data[mid] :
            return "yes"
        else :
            start = mid +1
    return "no"

for i in range(m) :
    result = binary_search(all_data, m_data[i], 0, n-1)
    print(result, end=" ")
    