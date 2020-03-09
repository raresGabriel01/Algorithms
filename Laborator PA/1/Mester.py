"""
Un meșter trebuie să paveze întreaga pardoseală a unei bucătării cu formă
dreptunghiulară de dimensiune L_1×L_2 centimetri, cu plăci de gresie
pătrate, toate cu aceeași dimensiune. Știind că meșterul nu vrea să taie nici o
placă de gresie și vrea să folosească un număr minim de plăci, să se
determine dimensiunea plăcilor de gresie de care are nevoie, precum și
numărul lor. De exemplu, dacă L_1=440 cm și L_2=280 cm, atunci meșterul
are nevoie de 77 de plăci de gresie, fiecare având latura de 40 cm.

"""

# Explicatii:

# Pentru determinarea numarului minim de placi, trebuie sa gasim dimensiunea optima a laturii unei placi
# dimensiunea optima a laturii unei placi e lungimea pentru care: numarul de placi incape "la fix"
# si nu exista o lungime mai mare care sa incapa "la fix" pentru dimensiunile bucatariei
# altfel spus, L1 si L2 trebuie sa se imparta fix la lungimea laturii unei placi
# si lungimea laturii unei placi sa fie maximala
# deducem ca lungimea laturii unei placi este cel mai mare divizor comun dintre L1 si L2


# Aplicam algoritmul lui Euclid prin scaderi repetate

l1 = int(input("Introduceti lungimea L1: ")) #citire
l2 = int(input("Introduceti lungimea L2: "))

arie = l1*l2 #calculam aria

l1,l2 = max(l1,l2),min(l1,l2) #facem aceasta interschimbare pentru a putea face scaderile fara grija ca obtinem un nr negativ

while l1 != l2:
    l1 -= l2                    #algoritmul lui Euclid
    l1, l2 = max(l1, l2), min(l1, l2)

#l1 are cum valoarea lungimii unei laturi de placa

numarNecesar = arie / (l1*l1) #impartind aria bucatariei la aria unei placi obtinem numarul necesar de placi

print("Latura unei placi:",l1)
print("Numarul necesar de placi:",numarNecesar)
