a= list(map(int, input().split()))
b= list(map(int, input().split()))
c= list(map(int, input().split()))
res_1 = max(abs(a[0]-c[0]), abs(a[1]-c[1]))
res_2 = abs(b[0]-c[0]) + abs(b[1]-c[1])
if res_1 > res_2 :
    print('daisy')
elif res_1 == res_2 :
    print('tie')
else : 
    print('bessie')