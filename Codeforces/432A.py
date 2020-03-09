#https://codeforces.com/problemset/problem/432/A
a, b = input().split()
n, k = int(a), int(b)
v = input().split()
l = []
for el in v:
    l.append(int(el)+k)
nr = 0
for el in l:
    if el <= 5:
        nr += 1
print(nr//3)
