import math
import sys
input = sys.stdin.readline


def isPrime(number):
    if number <= 1:
        return False
    sq = int(math.sqrt(number))

    for i in range(2, sq+1):
        if number % i == 0:
            return False

    return True


m, n = map(int, input().split())

for i in range(m, n+1):
    if isPrime(i):
        print(i)
