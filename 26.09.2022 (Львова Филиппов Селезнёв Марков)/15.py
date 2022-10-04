import random
lst=list(range(1,10000))
other = [i for i in
         range(7, 101, 3)
         if i%3!=0]
print(lst, other, sep='\n')
