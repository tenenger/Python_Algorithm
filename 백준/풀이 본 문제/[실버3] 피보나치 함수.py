t = int(input())
zero = [1, 0, 1] + ([0] * 40)
one = [0, 1, 1] + ([0] * 40)


for i in range(t):
    n = int(input())
    for j in range(2, n+1):
        zero[j] = zero[j-1] + zero[j-2]
        one[j] = one[j-1] + one[j-2]
    print(zero[n], one[n])
