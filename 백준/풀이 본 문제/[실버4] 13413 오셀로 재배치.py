t = int(input())
for _ in range(t):
    n = int(input())
    initial_ocello = list(input())
    target_ocello = list(input())
    arr = []
    for i in range(n):
        if initial_ocello[i] != target_ocello[i]:
            arr.append(initial_ocello[i])
    B_cnt = arr.count('B')
    W_cnt = arr.count('W')
    result = min(B_cnt, W_cnt) + abs(B_cnt - W_cnt)
    print(result)
