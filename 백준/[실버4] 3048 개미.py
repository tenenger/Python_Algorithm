import copy

n1_length, n2_lenght = map(int, input().split())
n1 = list(input())
n2 = list(input())
time = int(input())
cnt = 0
before = n1[::-1] + n2
after = copy.deepcopy(before)

while time != cnt:
    for i in range(n1_length + n2_lenght - 1):
        if before[i] in n1 and before[i+1] in n2:
            after[i], after[i+1] = after[i+1], after[i]
    before = copy.deepcopy(after)
    cnt += 1

print(''.join(before))
