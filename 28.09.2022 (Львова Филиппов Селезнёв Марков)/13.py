summ = int(input())
money = [1, 2, 4, 8, 16, 32, 64]
x = sum(money) + 1
b = []
while 1 <= (x := (x // 2)):
    n, summ = divmod(summ, x)
if n > 0:
    b.append(x * n)
    print(*b)
