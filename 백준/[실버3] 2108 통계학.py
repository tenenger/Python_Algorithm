import sys
def average(arr):
    return round(sum(arr) / len(arr))

def mid_value(arr):
    arr.sort()
    return arr[len(arr)//2]

def frequency(arr):
    if len(arr) == 1:
        return max(arr)
    dic = {}
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    modes = [key for key, value in dic.items() if value == max(dic.values())]
    modes.sort()
    if len(modes) >= 2:
        return modes[1]
    else:
        return max(modes)

def arround(arr):
    return max(arr) - min(arr)

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]
print(average(numbers), mid_value(numbers), frequency(numbers), arround(numbers))