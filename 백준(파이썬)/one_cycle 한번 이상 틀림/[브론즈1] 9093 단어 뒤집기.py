t = int(input())
result = []
for _ in range(t):
    st = input()
    st += " "
    for i in st:
        if i != " ":
            result.append(i)

        else:
            while result:
                print(result.pop(), end="")
            print(" ", end="")