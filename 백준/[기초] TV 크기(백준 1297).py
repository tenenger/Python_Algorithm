d, h, w = map(int, input().split())
rate = d / (w**2 + h**2)**(1/2)
a = (w * rate) // 1
b = (h * rate) // 1
print(int(b), int(a))