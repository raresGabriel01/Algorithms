n = int(input())
v = [0, 1]

i = 2

while i < n:
    v.append(v[i-1]+v[i-2])         # daca vrem sa fim mai eficienti dpdv al memoriei putem utiliza 3 variabile a1, a2 si a3
    i += 1                          # si la fiecare pas afisam val coresp

print(v)

