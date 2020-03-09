"""
Scrieți un program care să furnizeze toate cuvintele dintr-un șir de caractere formate din aceleași
litere cu ale unui cuvânt dat (fără a fi neapărat anagrame!). Dacă șirul nu conține nici un cuvânt cu
proprietatea cerută, programul trebuie să afișeze un mesaj corespunzător. Cuvintele din șir sunt
despărțite între ele prin spații și semnele de punctuație uzuale. De exemplu, pentru șirul “Langa o
cabana, stand pe o banca, un bacan a spus un banc bun.” și cuvântul “bacan” funcția trebuie să
furnizeze cuvintele “cabana”, “banca”, “bacan” și “banc”.
"""

#bagam literele cuvantului citit intr-un dictionar
#luam cuvant cu cuvant din text si verificam daca fiecare litera este cheie in dictionar
#daca este, afisam
#daca nu, mergem mai departe

file = open("input.txt","r")

# pentru simplitate, consideram primul cuvant din text (aflat singur, pe prima linie) ca fiind cuvantul dupa care cautam in text

word = file.readline()

d = {
                #laum un dictionar gol
}

for ch in word:
    if ch != "\n":      #punem literele lui word aici
        d[ch] = 1

l = [cuv for cuv in file.read().split()]        #lista cuvinte text



for cuv in l:       #pentru fiecare cuvant din lista

    d1 = {
                    #generam un dictionar gol
    }
    for ch in cuv.replace(",",""):      #ptr fiecare litera din cuvant (ignorand virgulele puse la finalul cuvantului)
            d1[ch] = 1                  #bagam litera in dictionar
    if d1 == d:                         #daca dictionarele sunt egale
        print(cuv.replace(",",""))      #afisam cuvantul
