n = int(input())
s = tmp = 2
for i in range(2, n+1):
    tmp *= 2*i*(2*i-1)//(i-1)
s += tmp
print(s)
