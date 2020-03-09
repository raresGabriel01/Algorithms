"""
8. Magazine și produse
Fișierul text “inventar.txt” conține pe fiecare rând, cu spațiu între ele, un șir de litere reprezentând
numele unui magazin, urmat de numere naturale reprezentând codurile produselor aflate în stoc
la acel magazin.
a) Stocați informațiile citite din fișier într-un dicționar având ca chei numele magazinelor și ca
valori un set cu codurile produselor din acel magazin.
b) Afișați codurile acelor produse care există în stocul tuturor magazinelor (intersecție de seturi).
c) Afișați codurile tuturor produselor (reuniune de seturi).
d) Afișați pentru fiecare magazin: numele magazinului și codurile produselor exclusiviste (produse
care se află doar în acel magazin, nu și în altele) (diferență de seturi).
"""

file = open("input.txt","r")

d = {

}

l = [cuv for cuv in file.read().split()]

numeMagazin = ""

for i in range(len(l)):                 #pentru fiecare cuv / litera
    if not l[i].isdigit():              # daca obiectul curent din lista nu este litera
        if i >= 1:                      #si daca nu e primul obiect
            if not l[i-1].isdigit():       #daca anteriorul a fost cuvant (in cazul in care numele magazinului e format din mai multe cuv)
                numeMagazin += l[i] + " "   #adaugam
            else:
                numeMagazin = l[i] + " "    #daca anteriorul a fost litera (adica am dat de un nou nume de magazin), reinitializam numeMagazin
        else :
            numeMagazin = l[i] + " "        # daca i = 1
    elif numeMagazin in d:              #adaugam in dictionar in mod corespunzator
        d[numeMagazin].append(l[i])
    else:
        d[numeMagazin] = [l[i]]

intersect = set(d[list(d.keys())[0]])           #folosim SET
#print(intersect)
for key in d:   #pentru fiecare cheie din d
    temp = {value for value in d[key] if value in intersect}    #intersectam d[cheie] cu intersectie
    intersect = temp    #atribuim corespunzator         #si retinem rezultatul

print(*intersect)


intersect = set()


for key in d:
    temp = {value for value in d[key]}
    intersect.update(temp)          #reunim

print(*intersect)

keyList = list(d.keys())

for i in range(len(keyList)):       #basically un "for in for" cu extra pasi
    print(keyList[i],end=" :")      #AL NAIBII DE URAT SI INEFICIENT
    for ob in d[keyList[i]]:        # dar mi-e somn, si e greu sa gasesc altceva acum, notat in TO DO LIST
        ok = True
        for j in range(len(keyList)):
            if j != i:
                for obj in d[keyList[j]]:
                    if ob == obj:
                        ok = False
        if ok == True:
            print(ob,end=" ")
    print()
