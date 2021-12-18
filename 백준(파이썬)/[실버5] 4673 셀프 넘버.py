def solution(n):
    numbers = list(map(str, range(1, n+1)))
    remove_list = []
    while True:
        for number in numbers:
            result = 0
            result += int(number)
            for i in number:
                result += int(i)
            if str(result) in numbers:
                remove_list.append(str(result))

        for j in remove_list:
            numbers[int(j)-1] = 0
        for k in numbers:
            if k == 0:
                continue
            else:
                print(k)
        break
            


solution(10000)