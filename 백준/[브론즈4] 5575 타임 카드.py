a, b, c = [list(map(int, input().split())) for i in range(3)]
for _ in (a,b,c) :
    enter = _[0] * 3600 + _[1] * 60 + _[2]
    out = _[3] * 3600 + _[4] * 60 + _[5]
    result = out - enter
    rest_h = result // 3600
    rest_m = (result % 3600) // 60
    rest_s = (result % 3600) % 60
    print(rest_h, rest_m, rest_s)