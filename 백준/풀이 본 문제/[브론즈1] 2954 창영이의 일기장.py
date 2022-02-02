def solution(string):
    arr = []
    answer = ''
    a = 'aeiou'
    index = 0
    while True:
        if string[index] in a:
            answer += string[index]
            index += 3
        else:
            answer += string[index]
            index += 1
        if index >= len(string):
            break
    return print(answer)

string = input()
solution(string)