"""
Se citește un șir format din n numere reale strict pozitive (n≥2), reprezentând
cursul de schimb valutar RON/EURO din n zile consecutive. Să se afișeze
zilele între care a avut loc cea mai mare creștere a cursului valutar, precum și
cuantumul acesteia. De exemplu, pentru n=6 zile și cursul valutar dat de șirul
4.25,4.05,4.25,4.48,4.30,4.40, cea mai mare creștere a fost de 0.23 RON,
între zilele 3 și 4.

"""

# vom citi cele n valori
# in timpul citirii, retinem diferentele
# daca o dfierenta determinata este o crestere mai mare decat cresterea maxima
# atunci o retinem pe aceasta drept crestere maxima

n = int(input("Introduceti numarul de zile: "))      #citire nr de zile

valAnt = float(input("Introduceti valoarea din ziua 1: ")) #citim primul numar in afara repetititei pentru a avea o val anterioara cu care sa lucram

crestereMaxima = 0 #cresterea maxima

z1, z2 = 0, 0 #zilele in care s-a inregistrat aceasta crestere


for zi in range (2,n+1):        #parcurgem
    valAct = float(input("Introduceti valoarea din ziua " + str(zi) +": "))     #citim
    if valAct - valAnt >= crestereMaxima: #daca cresterea e mai mare
        crestereMaxima = valAct - valAnt #o retinem
        z1 = zi-1       #si retinem si zilele
        z2 = zi
    valAnt = valAct     # la final, valoarea citita acum o sa devina anterioara pentru urmatoarea valoare

print("Cresterea maxima a fost de",crestereMaxima,"inregistrata intre zilele",z1,"si",z2) #afisare