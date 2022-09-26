x=[1,2,3,4,5,6,7,8,9,10,20,30,40]
for y in x:
    if y % 2 == 0:
        print(y)
    elif str(y).endswith('0'):
        print(y)
