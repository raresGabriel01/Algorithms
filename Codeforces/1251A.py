#https://codeforces.com/problemset/problem/1251/A

t = int(input())

l = []

for i in range(t):
    s = input()
    res = set()
    ress = ""
    lastCh = s[0]
    nr = 1
    for i in range(1,len(s)):
        if s[i] == lastCh:
            nr += 1
        else:
            if nr % 2 == 1 and lastCh not in res:
                res.add(lastCh)
                ress += lastCh
            lastCh = s[i]
            nr = 1

    if nr % 2 == 1 and lastCh not in res:
        res.add(lastCh)
        ress += lastCh

    l.append(''.join(sorted(ress)))



for r in l:
    print(r)

