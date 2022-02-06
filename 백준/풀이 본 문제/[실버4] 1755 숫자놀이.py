dictionary = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
              '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
n, m = map(int, input().split())
arr = []

for i in range(n, m+1):
    change_string = ' '.join(dictionary[x] for x in str(i))
    arr.append([i, change_string])

arr.sort(key=lambda x: x[1])

result = []
for i in arr:
    result.append(i[0])
for i in range(0, len(result), 10):
    print(' '.join(map(str, result[i:i+10])))
