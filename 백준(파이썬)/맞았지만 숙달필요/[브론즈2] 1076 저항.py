dictionary = {
'색' : ['black','brown','red','orange','yellow','green','blue','violet','grey','white'],
'값' : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
'곱' : [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
}
a = ''
for i in range(3):
    data = input()
    ind = dictionary['색'].index(data)
    if i == 2: 
        print(int(a) * dictionary['곱'][ind])
    else:
        a += str(dictionary['값'][ind])
    
