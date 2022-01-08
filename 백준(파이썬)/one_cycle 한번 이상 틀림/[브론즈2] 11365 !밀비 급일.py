while True:
    data = input()

    if data == "END":
        break

    else:
        data = list(reversed(data))
        print("".join(data))
        
