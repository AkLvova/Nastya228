n = int(input('Введите число 1<n≤10'))
f = 1
s = 0
for a in range(1, n+1):
    for b in range(1, a+1):
        f = f * b
s += f
print(s)
