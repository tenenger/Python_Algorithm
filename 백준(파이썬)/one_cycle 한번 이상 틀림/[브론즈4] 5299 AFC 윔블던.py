x, y = map(int, input().split())
a = int((x+y)/2)
b = x-a
if a < 0 or b < 0 or a+b != x or abs(a-b) != y :
    print(-1)
else :
    print(max(a,b), min(a,b))