n = int (input())

prim = []

i  = 2

while len(prim) < n :
    ok = True
    for x in prim :
        if x > int (i**0.5):
            break
        elif i % x == 0:
            ok = False
            break
    if ok: prim.append(i)
    i += 1

print(prim)

