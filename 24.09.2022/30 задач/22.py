x = int(input("число"))
f = x // 100
s = x % 100 // 10
print(s * 100 + f * 10 + x % 10)
