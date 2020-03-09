"""
Enunt prea lung - gasiti in PDF
"""

#pentru simplitate, afisam pe ecran

input = open("input.txt","r")



tipGraf = input.readline().replace("\n","")
x, y = input.readline().split()
n, m = int(x), int(y)

muchii = set()

for i in range(m):
    x, y = input.readline().split()
    muchii.add((int(x),int(y)))
x, y = input.readline().split()

s, f = int(x), int(y)

print(muchii)

d = {

}

for m in muchii:
    if m[0] in d:
        if m[1] not in d[m[0]]:         #as fi putut folosi SET, doar ca enuntul cere explicit LISTA
            d[m[0]].append(m[1])
    else:
        d[m[0]] = [m[1]]

    if tipGraf == "neorientat":         #daca e neorientat adaugam si invers
        if m[1] in d:
            if m[0] not in d[m[1]]:
                d[m[1]].append(m[0])
        else:
            d[m[1]] = [m[0]]

print(d)


matrice = []

for i in range(n+1):
    matrice.append([])
for i in range(n+1):
    for j in range(n+1):
        matrice[i].append(0)

for m in muchii:
    matrice[m[0]][m[1]] = 1
    if tipGraf == "neorientat":
        matrice[m[1]][m[0]] = 1

for i in range(1,n+1):
    for j in range(1, n+1):
        print(matrice[i][j],end=" ")
    print()


BF = []

BF.append((s,-1))

st, dr = 0, 0

while st <= dr:
    tata = BF[st][0]
    for fiu in d[tata]:                             #nu tocmai 100% eficient, dar respect indicatiile enuntului
        if fiu not in [nod for (nod,parinte) in BF]:
            BF.append((fiu, tata))
            dr += 1
    st += 1

print()

for tup in BF:
    print(tup[0],end=" ")

DF = []
vizitat = []

DF.append(s)
vizitat.append(s)

while DF != [] :
    tata = DF[-1]
    for fiu in d[tata]:
        if fiu not in vizitat:
            DF.append(fiu)
            vizitat.append(fiu)
    if tata == DF[-1]:
        DF.pop(-1)

print()

print(vizitat)

### nu inteleg cum vrea profa sa fac aia (e 12 noaptea, sunt rupt de oboseala)
### mult mai easy cun Dijkstra
### in TO DO LIST


