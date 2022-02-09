import sys
from math import sqrt
input = sys.stdin.readline


def check_square(arr):
    left_side = sqrt((arr[0][0] - arr[1][0])**2 + (arr[0][1] - arr[1][1])**2)
    bottom_side = sqrt((arr[0][0] - arr[2][0])**2 + (arr[0][1] - arr[2][1])**2)
    right_side = sqrt((arr[2][0] - arr[3][0])**2 + (arr[2][1] - arr[3][1])**2)
    top_side = sqrt((arr[1][0] - arr[3][0])**2 + (arr[1][1] - arr[3][1])**2)
    diagonal_side_1 = sqrt((arr[0][0] - arr[3][0])
                           ** 2 + (arr[0][1] - arr[3][1])**2)
    diagonal_side_2 = sqrt((arr[1][0] - arr[2][0])
                           ** 2 + (arr[1][1] - arr[2][1])**2)
    if left_side != bottom_side or bottom_side != right_side or right_side != top_side or top_side != left_side or diagonal_side_1 != diagonal_side_2:
        return 0
    else:
        return 1


t = int(input())
for i in range(t):
    data = [list(map(int, input().split())) for _ in range(4)]
    data.sort(key=lambda a: (a[0], a[1]))
    print(check_square(data))
