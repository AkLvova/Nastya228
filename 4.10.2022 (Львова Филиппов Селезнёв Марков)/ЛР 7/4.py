file = open(r'C:\Users\79642\Desktop\МДК\4.10.2022 (Львова Филиппов Селезнёв Марков)\ЛР 7\zadanie4.txt')

lines = 0
words = 0
symbols = 0

for line in file:
    lines += 1
    words += len(line.split())
    symbols += len(line.strip('\n'))

print("Lines:", lines)
print("Words:", words)
print("Symbols:", symbols)
