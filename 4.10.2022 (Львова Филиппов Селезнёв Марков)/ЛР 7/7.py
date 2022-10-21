

f=open('C:\Users\79642\Desktop\МДК\4.10.2022 (Львова Филиппов Селезнёв Марков)\ЛР 7\zadanie7.txt')  
f1=open('C:\Users\79642\Desktop\МДК\4.10.2022 (Львова Филиппов Селезнёв Марков)\ЛР 7\zadanie7a.txt','a')
b = f.readlines()
    
for word in (b):
    f1.write(word[::-1])


for worda in reversed(b):
    f1.write(worda[::-1])

f.close()
f1.close()

