import sys
print(set(map(str.rstrip, sys.stdin)))
a=list(input())
c = 0;
for i in a:
    for j in a:
        if i == j:
            c+=1
            c-=1
        print (c / 2)
