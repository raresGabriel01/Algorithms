"""
3. Folosind un dicționar, să se numere de câte ori apare fiecare caracter într-un text de tip "lorem
ipsum"
"""

file = open("input.txt", "r")

d = {

}

for c in file.read():           #aici verificam TOATE caracterele, inclusiv virgule, spatii, \n etc.
    if c in d:
        d[c] += 1
    else:
        d[c] = 1


print(d)