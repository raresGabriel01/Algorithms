"""
Să se determine cele mai mari două valori distincte dintr-un șir de numere întregi

Note: pentru aceasta problema si pentru urmatoarele, vom considera inputul dintr-in fisier numit "input.txt"
"""

file = open("input.txt","r")    #in fisier toate nr se afla pe aceeasi linie

l = [int(x) for x in file.read().split()]   #generam o lista cu toate elementele din fisier

max1, max2 = l[0], l[0] #initializam cu primul el din lista



for nr in l:      #ptr fiecare nr
    if nr > max1:                   #daca gasim un nou maxim "mare"
        max1, max2 = nr, max1       #schimbam
    elif nr > max2 and nr < max1:   #daca gasim un nou maxim "mic"
        max2 = nr                   #schimbam

print(max1,max2)                    #afisam

#complexitate O(n)
