import re

str_len = input()
string = input()
numbers = re.findall("\d+", string)
numbers = list(map(int, numbers))
print(sum(numbers))