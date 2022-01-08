t = int(input())
for i in range(t) :
    n = int(input())

    if n < 3 :
        for j in range(n) :
            print('#'*n)
        print()    
        
    else :
        print('#'*n)
        for k in range(n-2):
            print('#' + 'J'*(n-2) + '#')
        print('#'*n)
        print()