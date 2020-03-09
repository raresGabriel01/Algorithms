"""
Se citește un număr natural N.
a) Să se genereze și afișeze o matrice de dimensiune NxN, cu elementele de la 1 la N*N - în
ordine crescătoare, de la stânga la dreapta și de sus în jos.
b) Pentru a parcurge elementele matricei în spirală, pornind din colțul din stânga-sus (spre
dreapta, în jos, spre stânga, în sus, …), să se obțină întâi o listă având elemente de tip tuplu
(linie, coloană) care să reprezinte pozițiile ce trebuie parcurse în această spirală.
c) Folosind lista de tupluri de mai sus, să se afișeze elementele din matrice aflate la acele poziții.
"""

# --------- Desen in PDF-ul atasat -------------

n = int(input())

matrice = []

nr = 1

for i in range(n):
    matrice.append([])
    for j in range(n):
        matrice[i].append(nr)
        nr += 1

nr = 1

lc, cc = 0, 0
cd, lj, cst, ls = n-1, n-1, 0, 0

lTup = []

while nr <= n*n :
    for i in range (cc,cd):
        lTup.append((lc,i))
        nr += 1

    if n % 2 == 1 and lc ==ls and cc == cd:
        lTup.append((lc,cc))
        nr += 1
        break

    lc, cc = lc, cd
    cd -= 1



    for i in range(lc,lj):
        lTup.append((i,cc))
        nr += 1
    lc, cc = lj, cc
    lj -= 1

    for i in range(cc,cst,-1):
        lTup.append((lc,i))
        nr += 1
    lc, cc = lc, cst
    cst += 1

    for i in range(lc,ls,-1):
        lTup.append((i,cc))
        nr += 1
    lc, cc = ls+1, cc+1
    ls += 1


for tup in lTup:
    print(matrice[tup[0]][tup[1]],end=" ")