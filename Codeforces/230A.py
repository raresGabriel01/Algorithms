#https://codeforces.com/problemset/problem/230/A
a, b = input().split()
s, n = int(a), int(b)
l = []
for i in range(n):
    a, b = input().split()
    l.append((int(a),int(b)))
l.sort(key=lambda tup: tup[0])
ok = True
for el in l:
    if s>el[0]:
        s+=el[1]
    else:
        print("NO")
        ok = False
        break
if ok:
    print("YES")