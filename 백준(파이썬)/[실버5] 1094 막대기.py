n = int(input())
arr = [64]

while True:
    if n == sum(arr):
        break

    a = arr.pop()
    for _ in range(2):
        arr.append(a/2)
    
    if n <= sum(arr[:len(arr)-1]):
        arr.remove(min(arr))
print(len(arr))