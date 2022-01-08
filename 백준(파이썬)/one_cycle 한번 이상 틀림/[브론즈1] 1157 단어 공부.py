string = list(input().lower())
a='abcdefghijklmnopqrstuvwxyz'
d = [0]*30

for i in range(len(string)):
    d[a.index(string[i])] += 1

if d.count(max(d)) == 1:
    print(a[d.index(max(d))].upper()) 
else:
    print("?")