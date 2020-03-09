"""
Să se determine cuvântul care apare cel mai des într-o propoziție dată, precum și cuvântul care
apare cel mai rar. Dacă sunt mai multe posibilități, se vor afișa cuvintele cele mai mici din punct de
vedere lexicografic.
"""

file = open("input.txt","r")    #fisier

d = {
                                # un dictionar gol
}

l = [cuv for cuv in file.read().split()]    #generam lista

for cuv in l:                   #pentru fiecare cuv in lista
    if cuv in d:                #verific daca e in dictionar
        d[cuv] += 1             #daca e, ii mai adaug o prezenta
    else:
        d[cuv] = 1              #daca nu, o pun pe prima

keyMax, keyMin = l[0], l[0]     #initializam cheile pentru cuvantul care apare cel mai des, respectiv cel mai rar

for key in d:                   # pentru fiecare cheie din dictionar
    if d[key] > d[keyMax]:         #tratez fiecare caz posibil
        keyMax = key
    elif d[key] == d[keyMax] and key < keyMax:
        keyMax = key
    elif d[key] < d[keyMin]:
        keyMin = key
    elif d[key] == d[keyMin] and key < keyMin:
        keyMin = key

# complexitate O(n) (dict e un hashmap si key in d are compl O(1) )

print(keyMax, keyMin)