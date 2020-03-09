#https://codeforces.com/problemset/gymProblem/101149/B
n = int(input())
dr = []
for i in range(n):
    x, y = input().split()
    dr.append((int(x),int(y)))
dr.sort(key = lambda x: x[1])
nrActualSoldati = 0
nrNecesar = 0
for dragon in dr:
    var = dragon[0] - nrActualSoldati
    nrActualSoldati += var
    nrNecesar += var
    nrActualSoldati -= dragon[1]
print(nrNecesar)
####