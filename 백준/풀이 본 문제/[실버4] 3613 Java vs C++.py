import sys
input = sys.stdin.readline


def tojava(split_words):
    for word in split_words:
        for i in word:
            if i.isupper():
                return 'Error!'

    for i in range(len(split_words)):
        split_words[i] = split_words[i][0].upper() + split_words[i][1:]
    split_words[0] = split_words[0].lower()
    return ''.join(split_words)


def tocpp(words):
    result = ''
    for word in words:
        if word.islower():
            result = result + word
        else:
            result = result + '_' + word.lower()
    return result


string = input().strip()
split_string = string.split('_')
check_split_string = [x for x in split_string if x]
result = ''
if not string[0].islower():
    result = 'Error!'
elif len(check_split_string) != len(split_string):
    result = 'Error!'
else:
    if '_' in string:
        result = tojava(split_string)
    else:
        result = tocpp(string)
print(result)
