"""
Scrieți un program care citește de la tastatură un șir de caractere format din mai multe cuvinte,
separate printr-unul sau mai multe spații și îl modifică astfel încât fiecare cuvânt să înceapă cu literă
mare.
"""

#Vom utiliza metoda .title()

sir = input("Introduceti sirul: ")  #citire

sir = sir.title()   #metoda sir.title() returneaza stringul "sir" modificat, unde fiecare cuvant incepe cu litera mare (exact cerinta)

print(sir) #afisare