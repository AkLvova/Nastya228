with open(r"C:\Users\79642\Desktop\МДК\4.10.2022 (Львова Филиппов Селезнёв Марков)\ЛР 7\zadanie1.txt") as datfile:
    text = datfile.read()
    print(sum(map(int, text.split(None, 2)[:2])))
