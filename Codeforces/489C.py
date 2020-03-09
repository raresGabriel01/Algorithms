#https://codeforces.com/problemset/problem/489/C
x, y = input().split()
m, s = int(x), int(y)

l = [0] * m
vect = [0]*10

for i in range(m):
    l[i] = s//m

r = s % m

solutie = False

for i in range(m-1,-1,-1):
    l[i] += r
    r = 0
    if l[i] > 9:
        while l[i] > 9 :
            l[i] -= 1
            r += 1
i = m - 1
op = False
while i >= 0 and m != 1:
    while l[i] < 9 and l[i-1] > 0 :
        if i - 1 == 0:
            break
        l[i] += 1
        l[i - 1] -= 1
        op = True
    i -= 1
while op and m != 1:
    i = m - 1
    op = False
    while i >= 0:
        while l[i] < 9 and l[i - 1] > 0 :
            if i - 1 == 0:
                break
            l[i] += 1
            l[i - 1] -= 1
            op = True
        i -= 1
suma = 0
#print(*l)
for el in l:
    suma += el
if suma == s:
    solutie = True

for nr in l :
    vect[nr] += 1

aux = vect.copy()
nrMin, nrMax = 0, 0

for i in range(1,10):
    if vect[i] != 0:
        nrMin = nrMin * 10 + i
        vect[i] -= 1
        break
for i in range(10):
    while vect[i] > 0 :
        nrMin = nrMin * 10 + i
        vect[i] -= 1
for i in range(9,-1,-1):
    while aux[i] > 0 :
        nrMax = nrMax * 10 + i
        aux[i] -= 1
if s == 0 and m > 1:
    solutie = False

if solutie :
    print(nrMin, nrMax)
else :
    print(-1,-1)

