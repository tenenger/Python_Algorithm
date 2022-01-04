h, w = map(int,input().split())
data = [list(input()) for i in range(h)]
result = [ [-1]*w for i in range(h)]
cnt = 0

while cnt < w: 
    for j in range(h):
            for k in range(w):
                if data[j][k] == 'c' and result[j][k] == -1:
                    result[j][k] = cnt
    for i in data:
        i.pop()
        i.insert(0, '.')
    cnt += 1
for q in result:
    print(" ".join(map(str, q)))