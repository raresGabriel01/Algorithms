#https://codeforces.com/problemset/problem/1256/B
def rezolva(p,n):
    poz = [0]*(n+1)
    pot = [True]*(n+1)
    pot[0] = False
    for i in range(1,n+1):
        poz[perm[i]]=i
    i = 1
    nr = 0
    while i<=n and nr <= n-1:
        if poz[i] > i and pot[poz[i]-1]:
            nr += 1
            pot[poz[i] - 1] = False
            s = perm[poz[i]-1]
            #print("Retin in s numarul anterior lui ",i,"adica pe ", s)
            aux = perm[poz[i]-1]
            #print("Schimb ",aux,"si ",perm[poz[i]]," intre ele")
            perm[poz[i]-1]=perm[poz[i]]
            perm[poz[i]]=aux
           # print(perm)
            poz[i] -= 1
            poz[s] += 1
            #print("actualizez pozitia lui ",i,"ca fiind ",poz[i]," si pozitia lui ", s, " ca fiind ", poz[s])
            i -= 1
            #print()
        i += 1

q = int(input())
sol = []
for i in range(q):
    n = int(input())
    perm = [0]*(n+1)
    cv = input().split()
    for j in range(len(cv)):
        perm[j+1] = int(cv[j])
    rezolva(perm,n)
    #print(perm)
    sol.append(perm)
    #perm.clear()

for lista in sol:
    print(*lista[1:])