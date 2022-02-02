t = int(input())
for i in range(t):
    err = 'OK'
    arr = [0]*26
    m = input()
    for j in range(len(m)):
        arr[ord(m[j])-65] += 1
        if arr[ord(m[j])-65] == 3:
            try:
                if m[j+1] == m[j]:
                    arr[ord(m[j])-65] = -1
                    continue
                elif m[j+1] != m[j]:
                    err = 'FAKE'
                    break
            except Exception:
                err = 'FAKE'
    print(err)
