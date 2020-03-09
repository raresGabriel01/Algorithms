"""
Să se unifice două dicționare în care cheile sunt șiruri de caractere, iar valorile sunt de tip numeric.
Astfel, în rezultat va apărea fiecare cheie distinctă, iar pentru o cheie care apare în ambele
dicționare inițiale valoarea corespunzătoare va fi egală cu suma valorilor asociate cheii respective
în cele două dicționare
"""


d1 = {
         "rares":-1,
    "ana":2             #dictionarele care se vor umple cu date
}

d2 = {
    "ana":1,
    "gabriel":3
}

for key in d1:
    if key in d2:                       #luam cheile din primul dictionar si le bagam in al doilea
        d2[key] += d1[key]
    else:
        d2[key] = d1[key]

print(d2)