with open(r'C:\Users\79642\Desktop\МДК\4.10.2022 (Львова Филиппов Селезнёв Марков)\ЛР 7\zadanie3.txt') as f:
    print(*(sum(map(int, line.split())) for line in f.readlines()), sep='\n')
