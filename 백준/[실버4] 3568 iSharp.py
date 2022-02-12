data = input().split()
basic_type = data[0]
del data[0]

for s in data:
    alpha, string = '', ''
    s = s.replace(',', '').replace(';', '')

    for i in range(len(s)-1, -1, -1):
        if s[i].isalpha():
            alpha = s[i] + alpha
        elif s[i] == '[':
            string += ']'
        elif s[i] == ']':
            string += '['
        else:
            string += s[i]
    print(f'{basic_type}{string} {alpha};')
