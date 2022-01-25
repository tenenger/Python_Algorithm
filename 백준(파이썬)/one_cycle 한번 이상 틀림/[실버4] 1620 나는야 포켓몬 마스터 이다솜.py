import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
dict = {}

for i in range(1, n + 1):
    data = input().strip()
    dict[data] = i

dict_list = list(dict)

for i in range(m):
    question = input().strip()
    if question.isdigit():
        number = int(question)
        print(dict_list[number-1])
    else:
        print(dict[question])
