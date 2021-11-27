[기초-종합] 3 6 9 게임의 왕이 되자(설명)(py)

data = int(input())

for i in range(1, data+1) :
    count = 0
    for x in str(i) :
        if x =='3' or x == '6' or x == '9' :
            count += 1
    if count != 0 :
        print('X'*count, end=" ")    
    else :
        print(i, end=" ")