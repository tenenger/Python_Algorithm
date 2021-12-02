dictionary = {'Q1' : 0, 'Q2' : 0, 'Q3' : 0, 'Q4' : 0, 'AXIS' : 0}
n = int(input())

for i in range(n) :
    x, y = map(int, input().split())
    if x == 0 or y == 0 :
        dictionary['AXIS'] += 1
    else :
        if x >0 and y >0 :
            dictionary['Q1'] += 1
        elif x < 0 and y > 0 :
            dictionary['Q2'] += 1
        elif x < 0 and y < 0 :
            dictionary['Q3'] += 1
        else :
            dictionary['Q4'] += 1

for key in dictionary :
    print("{}: {}".format(key, dictionary[key]))