a=[1,2,3,4,5,6,7,8,9]

try:
    Sum_even = 0
    for i in range(0,len(a)+1,2):
        Sum_even+=a[i]
except IndexError:
    pass

try:
    Sum_odd = 0
    for j in range(1,len(a)+1,2):
        Sum_odd+=a[j]              
except IndexError:
    pass

print(Sum_even - Sum_odd)
