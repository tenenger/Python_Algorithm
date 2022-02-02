while True:
    n = int(input())
    if not n:
        break
    else:
        data = [input() for _ in range(n)]
        data.sort(key=lambda x: x.lower())
        print(data[0])