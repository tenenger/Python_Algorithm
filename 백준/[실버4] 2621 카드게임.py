import sys
input = sys.stdin.readline


def five_same_color(arr):
    arr = set(arr)
    if len(arr) == 1:
        return True
    else:
        return False


def sequence_number(arr):
    arr.sort()
    for i in range(4):
        if arr[i] + 1 in arr:
            continue
        else:
            return False
    return True


def how_same_number(arr, dict):
    if len(dict) == 2:
        if 4 in dict.values():
            for key, value in dict.items():
                if value == 4:
                    return [41, key]
        else:
            for key, value in dict.items():
                if value == 3:
                    max_key = key
                else:
                    min_key = key
            return [32, max_key, min_key]

    elif len(dict) == 3:
        if 3 in dict.values():
            for key, value in dict.items():
                if value == 3:
                    return [311, key]
        else:
            keys = []
            for key, value in dict.items():
                if value == 2:
                    keys.append(key)
            return [221, max(keys), min(keys)]

    elif len(dict) == 4:
        for key, value in dict.items():
            if value == 2:
                return [2111, key]
    else:
        return [11111, max(arr)]


max_result = 0
dictionary = {}
cards = [input().split() for _ in range(5)]
colors, numbers = [], []
for color, number in cards:
    colors.append(color)
    numbers.append(int(number))
    if int(number) in dictionary:
        dictionary[int(number)] += 1
    else:
        dictionary[int(number)] = 1

if five_same_color(colors):
    if sequence_number(numbers):
        result = 900 + max(numbers)
        max_result = max(max_result, result)

if len(how_same_number(numbers, dictionary)) == 2:
    a, b = how_same_number(numbers, dictionary)
    if a == 41:
        result = 800 + b
        max_result = max(max_result, result)

if len(how_same_number(numbers, dictionary)) == 3:
    a, b, c = how_same_number(numbers, dictionary)
    if a == 32:
        result = b*10 + c + 700
        max_result = max(max_result, result)

if five_same_color(colors):
    if not sequence_number(numbers):
        result = 600 + max(numbers)
        max_result = max(max_result, result)

if not five_same_color(colors):
    if sequence_number(numbers):
        result = 500 + max(numbers)
        max_result = max(max_result, result)
    else:
        if len(how_same_number(numbers, dictionary)) == 2:
            a, b = how_same_number(numbers, dictionary)
            if a == 311:
                result = 400 + b
                max_result = max(max_result, result)
            elif a == 2111:
                result = 200 + b
                max_result = max(max_result, result)
            else:
                result = 100 + b
                max_result = max(max_result, result)
        else:
            a, b, c = how_same_number(numbers, dictionary)
            if a == 221:
                result = b*10 + c + 300
                max_result = max(max_result, result)
print(max_result)
