#https://codeforces.com/problemset/problem/975/B
def sim(poz,l):
    if l[poz] <=14:
        aux = l[poz]
        l[poz]=0
        for i in range(1,aux+1):
            l[(poz+i)%14] += 1
    else:
        aux = l[poz]
        l[poz] = 0
        for i in range(14):
            l[i] += aux//14
        for i in range(1,aux%14+1):
            l[(poz+i)%14]+=1
def score(l):
    s = 0
    for i in range(14):
        if l[i]%2==0:
            s+=l[i]
    return s
l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])
v = l.copy()
maxim = 0

for i in range(14):
    sim(i,v)
   # print(v)
    if score(v) > maxim:
        maxim = score(v)
    v = l.copy()
print(maxim)