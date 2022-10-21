count = 0
eq = True
with open("C:\Users\79642\Desktop\МДК\4.10.2022 (Львова Филиппов Селезнёв Марков)\ЛР 7\zadanie8.txt", "r", encoding = "utf-8") as f1, open("C:\Programming\MDK\MDK_01_01\lr7_04_10\zadanie8\zadanie8a.txt", "r", encoding = "utf-8") as f2:
    for a1, a2 in zip(f1, f2):
        count += 1
        if a1 != a2:
            eq = False
            break

if eq == True:
    print("Нет отличий")
else:
    print("Отличается строка ", count)
