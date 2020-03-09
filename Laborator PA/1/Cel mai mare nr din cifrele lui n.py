"""
Se citește un număr natural nenul n. Să se afișeze cel mai mic și cel mare
număr ce pot fi formate din cifrele lui n. De exemplu, pentru n=812383 trebuie
afișate numerele 883321 și 123388.
"""

# Aceasta problema se rezolva utilizand un vector de frecventa
# luam pe rand cifrele numarului n
# si retinem intr-un vector aparitiile fiecarei cifre
# v[i]=c -----> inseamna ca cifra "i" apare de "c" ori in n
# dupa ce retinem cifrele, incepem sa "le punem la loc" in n, de la cea mai mare, la cea mai mica, pentru a obtine un numar maxim
# si invers pentru cel mai mic nr (ATENTIE LA ZEROURI)

n = int(input("Introduceti numarul: "))     # citim n

v = [0]*10      #declaram acel vector de frecventa

nrMax, nrMin = 0, 0     # numarul maxim, respectiv minim, initializate cu 0

while n != 0:
    v[n%10] += 1           #umplem vectorul de frecventa cu cifrele lui n
    n //= 10

for i in range (9,-1,-1):   #parcurgem de la mare la mic
    c = 1
    while c <= v[i]:    #cat timp mai exista cifra i
        nrMax = nrMax * 10 + i  #o adaugam
        c += 1

for i in range (1,10):  #parcurgem o singura data pentru a gasi un nr diferit de 0 sa-l bagam in fata ca sa nu avem 0 prima cifra
    if v[i] != 0:
        nrMin = nrMin * 10 + i
        v[i] -= 1
        break

for i in range (10):    #dparcurgem de la mic la mare (fara se ne mai ingrijoram ca am putea avea un 0 pe pozitie initiala)
    while v[i] != 0 :
        nrMin = nrMin * 10 + i  #consturim
        v[i] -= 1

print("Numarul maxim ce se poate obtine din cifrele lui n este:",nrMax) #afisam
print("Numarul minim ce se poate obtine din cifrele lui n este:",nrMin)
