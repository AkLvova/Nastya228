with open(r'C:\Users\79642\Desktop\МДК\4.10.2022 (Львова Филиппов Селезнёв Марков)\ЛР 7\zadanie2.txt') as f:
    print('yes' if input() in f.read() else 'no')
