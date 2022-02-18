import sys
input = sys.stdin.readline


def check(string, n, t, l):
    if string == 'O(N)':
        return n * t <= l * pow(10, 8)
    elif string == 'O(N^2)':
        return pow(n, 2) * t <= l * pow(10, 8)
    elif string == 'O(N^3)':
        return pow(n, 3) * t <= l * pow(10, 8)
    elif string == 'O(2^N)':
        return pow(2, n) * t <= l * pow(10, 8)
    else:
        # 실제로 팩토리얼을 돌리지 않고 중간에 넘으면 끝내도록 하면된다.
        # 안그러면 시간초과가 발생한다.
        multipy = t
        for i in range(1, n+1):
            multipy *= i
            if multipy > l * pow(10, 8):
                return False
        return True


dic = {}
c = int(input().strip())

for _ in range(c):
    string, n, t, l = input().strip().split()
    if check(string, int(n), int(t), int(l)) == True:
        print('May Pass.')
    else:
        print('TLE!')
