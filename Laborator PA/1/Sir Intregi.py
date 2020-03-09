"""Se citește un șir format din n numere întregi (n≥2). Să se afișeze cele mai mari
două valori distincte din șir sau mesajul "Imposibil", dacă acestea nu există."""

# Citim sirul
# in timp ce citim retinem cele mai mari 2 numere intregi
# atentie, DISTINCTE !

n = int(input("Introduceti numarul de numere citite: "))    #citim cate numere se citesc

max1 = int(input("Introduceti primul numar: "))             # citim primele 2 numere separat si le retinem in max1 si max2
max2 = int(input("Introduceti al 2-lea numar: "))

max1, max2 = max(max1,max2), min(max1,max2)         #initializam in functie de ele cele mai mari doua numere din sir
                                                    # max1 = cel mai mare nr , max2 = al doilea cel mai mare nr

for c in range(3,n+1): #parcurgem restul de numere
    nr = int(input("Introduceti al "+str(c)+"-lea numar: "))    #citim
    if nr > max1:   #daca gasim un numar strict mai mare decat cel mai mare numar
        max2 = max1 #atunci al doilea cel mai mare ia valoarea primului
        max1 = nr   #iar primul devine noul numar citit
    elif nr > max2 and nr < max1:   #daca gasim un nr strict mai mare decat al doilea cel mai mare, dar strict mai mic decat cel mai mare
        max2=nr #modificam valoarea celui de al doilea cel mai mare

print("Cele mai mari 2 numere distincte sunt:",max1,max2) #afisam solutia