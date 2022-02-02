while True:
    try:
        data = input()

        d = [0]*4

        for i in list(data):
            if i.isdigit():
                d[2] += 1
            elif i.isspace():
                d[3] += 1
            elif i.isupper():
                d[1] += 1
            elif i.islower():
                d[0] += 1

        print(" ".join(map(str, d)))
    except EOFError:
        break
