s = input()
alpha_list = ['ABC',"DEF","HIG","JKL","MNO","PQRS","TUV","WXYZ"]

time = 0
for i in alpha_list:
    for j in s :
        if j in i :
            time += alpha_list.index(i) +3 
print(time)
