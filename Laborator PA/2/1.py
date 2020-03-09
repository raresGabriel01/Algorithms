"""
Într-o propoziție/frază a fost efectuată, posibil de mai multe ori, aceeași greșeală de ortografie.
Scrieți un program care citește propoziția, șirul greșit și șirul corect, după care afișează propoziția
corectă. De exemplu, în propoziția “Problemele cu șiruri de caractedf nu sunt gdfle!” greșeală constă
în faptul că în loc de șirul “re” a fost scris șirul “df”.
"""

#Utilizam metoda replace()

sir = input("introduceti sirul: ")
gresit = input("Introduceti greseala: ")        #citiri
corect = input("Introduceti varianta corecta: ")

sir = sir.replace(gresit,corect)    # utilizam metoda replace()

# metoda sir.replace(x,y,z) returneaza stringul "sir" modificat, unde substringul x este inlocuit de substringul y de z ori
# daca z nu este precizat, atunci se inlocuiesc by-default toate paritiile lui x cu y

print(sir)  #afisare