n = int(input())
max1 = max(n % 10, n // 10)
check = False
if max1 == n // 10 != n % 10:
    check = True
    print('Первая цифра числа больше')
elif max1 == n % 10 != n // 10:
        check = True
        print('Вторая цифра числа больше')
        if not check:
            print('Цифры числа одинаковы')
        else:
                print('Цифры числа различны')
