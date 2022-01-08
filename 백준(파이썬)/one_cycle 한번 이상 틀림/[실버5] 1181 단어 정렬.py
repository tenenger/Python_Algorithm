n = int(input())
data = [input() for _ in range(n)]

a = list(set(data))
a.sort()
a.sort(key=len)
print("\n".join(a))
