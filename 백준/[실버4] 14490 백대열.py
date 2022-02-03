import math
n, m = map(int, input().split(':'))
result = math.gcd(n, m)
print(f'{int(n/result)}:{int(m/result)}')
