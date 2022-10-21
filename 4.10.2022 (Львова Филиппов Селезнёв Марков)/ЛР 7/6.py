wordlist = []
f = open("C:\Users\79642\Desktop\МДК\4.10.2022 (Львова Филиппов Селезнёв Марков)\ЛР 7\zadanie6.txt",'r')
for word in f.readlines():
    wordlist.append(word.strip())

# Ищем номер самой длинной строки
dl = 0
number = 0
length = 0
for i in range(len(wordlist)):
    if len(wordlist[i]) > length:
        length = len(wordlist[i])
        dl = len(wordlist[i])
        line = wordlist[i]
        number = i
f. close()        
print("а) " + str(number),"б) " + str(dl),"в) " +  line, sep="\n")
