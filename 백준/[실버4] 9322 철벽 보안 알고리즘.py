testcase = int(input())

for _ in range(testcase):
    string_cnt = int(input())
    no1_public_key = input().split()
    no2_public_key = input().split()
    security_statement = input().split()
    result = [''] * string_cnt

    for i in range(string_cnt):
        idx = no1_public_key.index(no2_public_key[i])
        result[idx] = security_statement[i]

    print(' '.join(result))
