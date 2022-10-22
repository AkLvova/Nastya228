import math
x = int(input())
y = int(input())
def t2(x, y):    
    z1 = ((2*x)-(math.cos(y+1)))
    z2 = (y + (math.sin(x+0.4)))
    print(z1)
    print(z2)

t2(x, y)
