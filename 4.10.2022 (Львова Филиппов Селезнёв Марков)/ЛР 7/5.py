file = 'C:\Users\79642\Desktop\МДК\4.10.2022 (Львова Филиппов Селезнёв Марков)\ЛР 7\zadanie5.txt'
action = input("Введите значение от а до д: ").lower() #а б в г д
with open(file) as f:
    data = f.readlines()
    if action == 'а':
        print(data[0])
    elif action == 'б':
        print(data[4])
    elif action == 'в':
        print(*data[0:5])
    elif action == 'г':
        s1, s2 = map(int, input('Введите s1 и s2 через пробел: ').split())
        print(*data[s1-1 : s2-0])
    elif action == 'д':
        print(*data)
