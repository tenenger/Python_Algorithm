'''
이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
'''

n = int(input())
a = {}
a[''] = 
def fibonacci(n) :
    if n == 1 :
        return a['fibonacci(n)'] = 1
    elif n == 2 :
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(n+1))