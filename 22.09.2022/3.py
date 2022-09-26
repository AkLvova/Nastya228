n=int(input())
n1 = n//100
n2 = n//10%10
n3 = n%10
if n1 == n2 == n3:
    print("все цифры одинаковы")
else:
    print("не одинаковы")
    if n1 == n2 or n1 == n3 or n2 == n3:
        print("есть одинаковые")
    else:
        print("нет одинаковых")

