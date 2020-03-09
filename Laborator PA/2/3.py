"""
Scrieți un program care să înlocuiască într-o propoziție toate aparițiile unui cuvânt 𝑠𝑠 cu un cuvânt
𝑡𝑡. Atenție, NU se poate utiliza metoda replace! De ce?
"""

# nu putem utiliza functia replace in mod corespunzator in aceasta problema
# un motiv este faptul ca t poate fi un substring al lui s
# Exemplu:
# sir = "Ionel si Ion sunt colegi"
# s = "Ion"
# t = "Gigel"
# daca utilizam functia replace, output-ul va arata astfel : "Gigelel si Gigel sunt colegi", ceea ce nu ne dorim
# pentru aceasta situatia, vom utiliza metoda .split()

sir = input("Introduceti sirul: ")
s = input("Introduceti sirul de inlocuit: ")            #citim
t = input("Introduceti sirul cu care va fi inlocuit s: ")

sirFinal = ''       #in acest sir o sa punem sirul rezultat final in urma modificarilor

for cuv in sir.split():     # pentru fiecare cuvant din lista de cuvinte (explicatii .split() mai jos)
    if cuv == s:            # daca cuvantul nostru este cel de inlocuit
        sirFinal += t       # ii punem inlocuitorul in sirul final
    else:
        sirFinal += cuv        #altfel adaugam cuvantul
    sirFinal += ' '         #adaugam spatii ptr a separa cuvintele intre ele

print(sirFinal)             #afisare

# Explicatii functia .split()
# sir.split(sep) returneaza o lista ce contine cuvintele sirului sir, delimitate de separatorul sep
# daca sep nu este mentionat, atunci by-default se considera spatiul ca separator