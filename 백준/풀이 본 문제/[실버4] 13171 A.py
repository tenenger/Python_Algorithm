import sys
input = sys.stdin.readline
a = int(input())
x = int(input())

# 고속 거듭제곱 알고리즘


def fast_pow(a, x):
    result = 1
    while x:
        if x % 2:
            result = (result * a) % (pow(10, 9) + 7)
        x //= 2
        a *= a % (pow(10, 9) + 7)
    return result


print(fast_pow(a, x))
