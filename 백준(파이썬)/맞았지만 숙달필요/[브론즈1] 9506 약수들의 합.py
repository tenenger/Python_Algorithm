while True:
    n = int(input())
    data = []
    if n == -1:
        break
    else:
        for i in range(1, n//2+1):
            if n % i == 0:
                data.append(i)
        if sum(data) == n:
            print(f"{n} = " + " + ".join(map(str, data)))
        else:
            print(f"{n} is NOT perfect.")